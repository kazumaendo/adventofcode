import argparse
from pathlib import Path
from models.santa_string import SantaString

def main() -> None:
    parser = argparse.ArgumentParser(description="Solve for first or second solution.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    args = parser.parse_args()
    santa_string = SantaString()

    if args.first:
        input_file_name = Path(__file__).parent/"example_inputs"/"input1.txt"
        with open(input_file_name) as f:
            for line in f:
                santa_string.read_string(line)
        print(f"Output: {santa_string.puzzle_output}")
    elif args.second:
        print()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
