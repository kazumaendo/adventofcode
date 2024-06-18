import argparse
from pathlib import Path
from models.parse_json import JSONParser


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve for first or second solution.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    args = parser.parse_args()

    if args.first:
        jsonl_txt_file = Path(__file__).parent/"example_inputs"/"input1.txt"
        with open(jsonl_txt_file) as f:
            for line in f:
                JSONParser(line)
    elif args.second:
        print()
    elif args.test:
        # import unittest
        # from tests.assert_example import TestFunction
        # test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction)
        # unittest.TextTestRunner().run(test_suite)
        jsonl_txt_file = Path(__file__).parent/"example_inputs"/"test_data.txt"
        with open(jsonl_txt_file) as f:
            for line in f:
                JSONParser(line)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
