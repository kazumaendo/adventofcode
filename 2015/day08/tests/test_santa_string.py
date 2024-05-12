import unittest
from ..models.santa_string import SantaString
from pathlib import Path

class SantaStringTestCase(unittest.TestCase):
    def test_get_string_literal_to_memory_diff_empty(self):
        santa_string = SantaString()
        input = r''

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,2)

    def test_get_string_literal_to_memory_diff_simple(self):
        santa_string = SantaString()
        input = r'due834mx02,854ndfk'

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,2)

    def test_get_string_literal_to_memory_diff_escape_slash(self):
        santa_string = SantaString()
        input = r'\\\\\\\\\\\\'

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,8)

    def test_get_string_literal_to_memory_diff_escape_quote(self):
        santa_string = SantaString()
        input = r'\"\"\"\"\"\"'

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,8)

    def test_get_string_literal_to_memory_diff_hexadecimal(self):
        santa_string = SantaString()
        input = r'\xfe,x\x3b'

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,8)
    
    def test_get_string_literal_to_memory_diff_mix(self):
        santa_string = SantaString()
        input = r'\"\\\"\xfe,x\"\x3b'

        result = santa_string.get_string_literal_to_memory_diff(input)

        self.assertEqual(result,12)
    