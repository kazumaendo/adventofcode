import unittest
from solution import string_is_nice
import json
from pathlib import Path

class TestFunction(unittest.TestCase):
    def test_find_floor(self):
        test_data_path = Path(__file__).parent/"test_data.json"
        with open(test_data_path) as json_file:
            test_data = json.load(json_file)
        
        for test_case in test_data:
            self.assertEqual(string_is_nice(test_case["input"]), test_case["expected_output"])

if __name__ == '__main__':
    unittest.main()