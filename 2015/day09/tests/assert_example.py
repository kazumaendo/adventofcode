import unittest
from pathlib import Path
from models.map import Map

class TestFunction(unittest.TestCase):
    def test_instructions(self):
        test_data_path = Path(__file__).parent.parent/"example_inputs"/"test_data.txt"
        map = Map(test_data_path)
        shortest_path = map.find_shortest_distance_to_cover_all_cities()
        self.assertEqual(shortest_path, 605)