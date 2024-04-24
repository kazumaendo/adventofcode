import argparse

def right_rectangular_prism_dimension(l: int, w: int, h: int) -> int:
    return 2*l*w+2*w*h+2*h*l

def min_area(l: int, w: int, h: int) -> int:
    return min(l*w, w*h,h*l)

def wrapping_paper_order(dimensions: str) -> int:
    l,w,h=map(int, dimensions.split('x'))
    return right_rectangular_prism_dimension(l,w,h) + min_area(l,w,h)

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
        result = wrapping_paper_order(args.input_string)
        print(f"Input: {args.input_string}\nResult: {result}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
