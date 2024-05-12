import unittest
from ..models.santa_string import SantaString
from pathlib import Path

class TestFunction(unittest.TestCase):
    def test_instructions(self):
        santa_string = SantaString()
        test_data_path = Path(__file__).parent.parent/"example_inputs"/"test_data.txt"
        with open(test_data_path) as test_data:
            for line in test_data:
                santa_string.read_string(line)
        self.assertEqual(santa_string.puzzle_output, 12)