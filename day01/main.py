#!/usr/bin/env python3
from pathlib import Path


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def find_components_in_list(numbers: list[int], equal_to: int=2020):
    for val in numbers:
        required = equal_to - val
        if required in numbers and required != val:
            return val, required


def solve(lines: list[str]) -> tuple[int, int]:
    inputs = sorted([int(x) for x in lines if int(x)<2000])
    comps = find_components_in_list(inputs)
    def find_3components():
        for n in inputs:
            comps2 = find_components_in_list(inputs, 2020-n)
            if sum(comps2, n) == 2020:
                comps2 += n,
                return comps2
    result = comps[0] * comps[1]
    # two stars
    comps3 = find_3components()
    result3 = comps3[0] * comps3[1] * comps3[2]
    return result, result3


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
