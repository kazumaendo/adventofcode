class LookAndSay():
    def __init__(self, initial_value: int) -> None:
        self._value = str(initial_value)

    def create_next_sequence(self) -> None:
        string_iterator = iter(self.value)
        previous_char = next(string_iterator)
        repetition_counter = 1
        next_sequence = ""

        for current_char in string_iterator:
            if current_char == previous_char:
                repetition_counter+=1
            else:
                next_sequence+=f"{repetition_counter}{previous_char}"
                previous_char = current_char
                repetition_counter = 1
        next_sequence+=f"{repetition_counter}{previous_char}"
        self.value = next_sequence

    def create_sequence_with_repetition(self, repetition_count: int):
        for _ in range(repetition_count):
            self.create_next_sequence()
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def length(self):
        return len(self.value)