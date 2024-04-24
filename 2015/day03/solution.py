import argparse

def houses_with_present(commands: str) -> int:
    houses = 1
    longitude,latitude = 0,0
    delivered = {(0,0)}
    for command in commands:
        match command:
            case '<':
                longitude-=1
            case '^':
                latitude+=1
            case '>':
                longitude+=1
            case 'v':
                latitude-=1
        if (longitude,latitude) not in delivered:
            delivered.add((longitude,latitude))
            houses+=1
    return houses

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
        result = houses_with_present(args.input_string)
        print(f"Input: {args.input_string}\nResult: {result}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
