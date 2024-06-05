class LookAndSay():
    def __init__(self, initial_value: int) -> None:
        self.value = str(initial_value)

    def create_next_sequence(self) -> None:
        # ex: 111221
        # Iterate through the value left to right
        # Keep track of the previous value and the count of repetition (if it is a consecutive value: value == previous_value, increment counter. if not then reset counter and previous value before stepping to next value)
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