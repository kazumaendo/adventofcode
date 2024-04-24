import argparse

def find_floor(input: str) -> int:
    up_count, down_count = 0,0
    for char in input:
        match char:
            case '(':
                up_count+=1
            case ')':
                down_count+=1
    return up_count - down_count

def main() -> None:
    parser = argparse.ArgumentParser(description="Process input string or run tests.")
    parser.add_argument("input_string", nargs="?", help="Input string to process.")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    args = parser.parse_args()

    if args.test:
        import unittest
        from test import TestFunction
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction)
        unittest.TextTestRunner().run(test_suite)
    elif args.input_string:
        result = find_floor(args.input_string)
        print(f"Input: {args.input_string}\nResult: {result}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()