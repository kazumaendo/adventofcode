import argparse
from itertools import product
from pathlib import Path
import re
from typing import Optional, Tuple
import logging

class CartesianCoordinate:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y

class Grid:
    def __init__(self):
        self.lights = set()
    
    def __len__(self):
        return len(self.lights)

    def generate_grid(self, pointA: CartesianCoordinate, pointB: CartesianCoordinate):
        return product(range(pointA.x, pointB.x+1), range(pointA.y, pointB.y+1))

    def parse_command(self, command:str) -> Optional[Tuple[str, str, str, str, str]]:
        pattern = r'(\w+)\s+(\d+),(\d+)\s+through\s+(\d+),(\d+)'
        matches = re.findall(pattern,command)
        return matches[0] if matches else None

    def toggle_lights(self, pointA: CartesianCoordinate, pointB: CartesianCoordinate):
        grid = set(self.generate_grid(pointA,pointB))
        toggle_on = grid - self.lights
        self.lights.difference_update(grid & self.lights)
        self.lights.update(toggle_on)

    def turn_lights_on(self, pointA: CartesianCoordinate, pointB: CartesianCoordinate):
        self.lights.update(self.generate_grid(pointA,pointB))

    def turn_lights_off(self, pointA: CartesianCoordinate, pointB: CartesianCoordinate):
        self.lights.difference_update(self.generate_grid(pointA,pointB))

    def count_lit_cells(self, input: str) -> None:
        input_parsed = self.parse_command(input)
        try:
            command_type, x1, y1, x2, y2 = input_parsed[0], *(int(i) for i in input_parsed[1:])
            pointA = CartesianCoordinate(x1,y1)
            pointB = CartesianCoordinate(x2,y2)
        except Exception as e:
            logging.error(f"'{e}' occured. Input is not in the right format.")

        match command_type:
            case 'toggle':
                self.toggle_lights(pointA, pointB)
            case 'off':
                self.turn_lights_off(pointA, pointB)
            case 'on':
                self.turn_lights_on(pointA, pointB)
        return


def main() -> None:
    parser = argparse.ArgumentParser(description="Process input string or run tests.")
    parser.add_argument("input_string", nargs="?", help="Input string to process.")
    parser.add_argument("--test", action="store_true", help="Run tests.")
    parser.add_argument("--first", action="store_true", help="Solve first problem")
    parser.add_argument("--second", action="store_true", help="Solve second problem")
    args = parser.parse_args()
    grid = Grid()

    if args.test:
        import unittest
        from test import TestFunction
        test_suite = unittest.TestLoader().loadTestsFromTestCase(TestFunction)
        unittest.TextTestRunner().run(test_suite)
    elif args.input_string:
        grid.count_lit_cells(input=args.input_string)
        result = grid.__len__()
        print(f"Input: {args.input_string}\nResult: {result}")
    elif args.first:
        input_file_name = Path(__file__).parent/"input1.txt"
        with open(input_file_name) as f:
            for line in f:
                grid.count_lit_cells(input=line)
        lit_count = grid.__len__()
        print(f"Number of lit grids: {lit_count}")
    elif args.second:
        print()
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
