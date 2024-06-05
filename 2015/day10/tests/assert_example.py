import unittest
from models.look_and_say import LookAndSay

class TestFunction(unittest.TestCase):
    def test_instructions(self):
        expected = ["11","21","1211","111221","312211"]
        sequence = LookAndSay(1)
        self.assertEqual(sequence.value, "1")
        for i in range(5):
            sequence.create_next_sequence()
            self.assertEqual(sequence.value, expected[i])
