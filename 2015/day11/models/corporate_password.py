class CorporatePassword():
    INVALID_LETTERS = ['i', 'o', 'l']

    def __init__(self, password: str) -> None:
        self._password = password

    def get_next_valid_password(self):
        while not self.is_valid_password():
            self.increment_password()
        return self._password

    def increment_password(self):
        password = list(self._password)
        current_idx = len(password)-1
        while current_idx >= 0:
            if password[current_idx] == 'z':
                password[current_idx] = 'a'
                current_idx -= 1
            else:
                password[current_idx] = chr(ord(password[current_idx]) + 1) # noqa
                break
        else:
            password.insert(0, 'a')
        incremented_password = ''.join(password)
        # TODO: create a setter
        self._password = incremented_password
        return incremented_password

    def is_valid_password(self) -> bool:
        prev_letter_pair_idx: int | None = None
        pair_count = 0
        has_increasing_three_letters = False
        self.validate_password_length()
        for i in range(len(self._password)):
            if self._password[i] in self.__class__.INVALID_LETTERS:
                return False
            if pair_count < 2 and i+1 < len(self._password):
                if (not prev_letter_pair_idx or prev_letter_pair_idx != i) \
                    and self._password[i] == self._password[i+1]: # noqa
                    pair_count += 1
                    prev_letter_pair_idx = i+1
            if not has_increasing_three_letters and i+2 < len(self._password):
                has_increasing_three_letters = \
                    self.is_increasing_straight(self._password[i:i+3])
        return (pair_count >= 2) and has_increasing_three_letters

    def validate_password_length(self) -> bool:
        if len(self._password) != 8:
            return False

    def is_increasing_straight(self, sub_str: str) -> bool:
        return ord(sub_str[1]) == ord(sub_str[0])+1 and \
            ord(sub_str[2]) == ord(sub_str[1])+1

    def is_pair(self, sub_str: str) -> bool:
        return sub_str[0] == sub_str[1]
