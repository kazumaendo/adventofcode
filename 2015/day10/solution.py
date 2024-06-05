import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Solve for first or second solution.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    args = parser.parse_args()

    if args.first:
        pass
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
