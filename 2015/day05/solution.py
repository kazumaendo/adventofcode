import argparse
from pathlib import Path

def string_is_nice(input: str) -> bool:
    naughty_pair = {"ab","cd","pq","xy"}
    vowels = {"a","e","i","o","u"}
    vowel_count = 1 if input[0] in vowels else 0
    double_letter = 0

    for char1, char2 in zip(input, input[1:]):
        if char2 in vowels:
            vowel_count+=1
        if char1 == char2:
            double_letter+=1
        if (char1+char2) in naughty_pair:
            return False
    
    if vowel_count >= 3 and double_letter:
        return True
    return False

def string_is_nice_updated(input: str) -> bool:
    return False

def main() -> None:
    parser = argparse.ArgumentParser(description="Process input string or run tests.")
    parser.add_argument("input_string", nargs="?", help="Input string to process.")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    args = parser.parse_args()

    if args.test:
        import unittest
        from test import TestFunction
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction)
        unittest.TextTestRunner().run(test_suite)
    elif args.input_string:
        result = string_is_nice(args.input_string)
        print(f"Input: {args.input_string}\nResult: {result}")
    elif args.first:
        nice_str_count=0
        input_file_name = Path(__file__).parent/"input1.txt"
        with open(input_file_name) as f:
            for line in f:
                nice_str_count+=1 if string_is_nice(line.strip()) else 0
        print(f"Number of nice strings: {nice_str_count}")
    elif args.second:
        print()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
