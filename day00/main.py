#!/usr/bin/env python3
from pathlib import Path
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def solve(lines: list[str]) -> tuple[int, int]:
    """
    Insert solution here
    """
    return part1, part2

def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    print("Part two:", solution[1])


if __name__ == "__main__":
    main()
