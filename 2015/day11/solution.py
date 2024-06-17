import argparse
from models.corporate_password import CorporatePassword


def main() -> None:
    parser = argparse.ArgumentParser(description="Solve for first or second solution.") # noqa
    parser.add_argument("--first", action="store_true", help="Solve first problem") # noqa
    parser.add_argument("--second", action="store_true", help="Solve second problem") # noqa
    parser.add_argument("--test", action="store_true", help="Run tests.")
    args = parser.parse_args()

    if args.first:
        input = "hepxcrrq"
        corporate_password = CorporatePassword(input)
        print(f"next valid password: {corporate_password.get_next_valid_password()}") # noqa
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
