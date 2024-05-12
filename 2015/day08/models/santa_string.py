import re


class SantaString:
    def __init__(self) -> None:
        self.puzzle_output = 0
    
    def read_string(self, string_literal: str):
        self.puzzle_output += self.get_string_literal_to_memory_diff(string_literal)
    
    def get_string_literal_to_memory_diff(self, string_literal: str) -> int:
        extra_character_count = 2
        pattern = r'(\\{2}|\\\"|\\x[0-9a-fA-F]{2})'
        matches = re.findall(pattern, string_literal)
        for m in matches:
            match m:
                case '\\\\' | '\\\"':
                    extra_character_count+=1
                case _:
                    extra_character_count+=3
        return extra_character_count

