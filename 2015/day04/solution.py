import argparse
import hashlib

def find_lowest_md5_hash(input: str) -> int:
    i=1
    while hashlib.md5((input+str(i)).encode()).hexdigest()[:6] != '000000':
        i+=1
    return i

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
        result = find_lowest_md5_hash(args.input_string)
        print(f"Input: {args.input_string}\nResult: {result}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
