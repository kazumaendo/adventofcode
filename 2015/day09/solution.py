import argparse
from pathlib import Path
from models.map import Map

def main() -> None:
    parser = argparse.ArgumentParser(description="Solve for first or second solution.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    args = parser.parse_args()

    if args.first:
        input_file_name = Path(__file__).parent/"example_inputs"/"input1.txt"
        map = Map(input_file_name)
        shortest_path = map.find_shortest_distance_to_cover_all_cities()
        print(f"Shortest path: {shortest_path}")
    elif args.second:
        print()
    elif args.test:
        import unittest
        from tests.assert_example import TestFunction
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction)
        unittest.TextTestRunner().run(test_suite)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
