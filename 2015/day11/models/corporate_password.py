class CorporatePassword():
    INVALID_LETTERS = ['i','o','l']
    def __init__(self, password: str) -> None:
        self._password = password

    def get_next_valid_password(self):
        while not self.is_valid_password():
            self.increment_password
        pass

    def increment_password(self):
        pass

    def is_valid_password(self) -> bool:
        self.validate_password_length()
        string_iterator = iter(self._password)
        for c in string_iterator:
            if c in self.__class__.INVALID_LETTERS:
                return False
            
        return True

    def validate_password_length(self) -> bool:
        if len(self._password) != 8:
            return False
