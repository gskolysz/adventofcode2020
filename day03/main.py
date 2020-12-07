#!/usr/bin/env python3
from functools import reduce
from pathlib import Path
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def solve(lines: list[str]) -> tuple[int, int]:
    piece_width = len(lines[0])
    piece_height = len(lines)

    def is_tree(char):
        return char == "#"

    def count_trees(move_x, move_y):
        x, y = 0, 0
        trees = 0
        for i in range(piece_height):
            x += move_x
            x = x % piece_width
            y += move_y
            if y >= piece_height:
                break

            if is_tree(lines[y][x]):
                trees += 1
        return trees

    trees_per_slope = []
    # part1 
    trees = count_trees(3, 1)

    # part2
    for move_x, move_y in [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]:
        trees_per_slope.append(count_trees(move_x, move_y))

    multiplies = reduce(lambda a, b: a*b, trees_per_slope)
    return trees, multiplies


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
