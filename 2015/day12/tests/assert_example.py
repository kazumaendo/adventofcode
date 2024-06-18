import unittest
from pathlib import Path
from models.parse_json import JSONParser


class TestFunction(unittest.TestCase):
    def test_instructions(self):
        idx = 0
        answers = [6, 6, 3, 3, 0, 0, 0, 0]
        jsonl_txt_file = Path(__file__).parent.parent/"example_inputs"/"test_data.txt"
        with open(jsonl_txt_file) as f:
            for line in f:
                JSONParser(line)
                ans = answers[idx]
                idx += 1
        self.assertEqual(shortest_path, 605)
