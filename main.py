#!/usr/bin/env python3
from collections import Counter
from functools import reduce
from itertools import chain
from pathlib import Path
from typing import Union


def load_input_lines(filename: Union[str, int]) -> list[any]:
    full_path = Path(__file__).resolve().parent / "inputs" / str(filename)
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def find_components_in_list(numbers: list[int], equal_to: int=2020):
    for val in numbers:
        required = equal_to - val
        if required in numbers and required != val:
            return val, required

def resolve_day1():
    inputs = load_input_lines(1)
    inputs = sorted([int(x) for x in inputs if int(x)<2000])
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


def parse_policy(line: str) -> tuple[int, int, str, str]:
    minmax, char, passwd = line.split(" ")
    min_o, max_o = minmax.split("-")
    char = char.strip(":")

    return int(min_o), int(max_o), char, passwd


def is_passwd_valid(min_o, max_o, char, passwd) -> bool:
    ctr = Counter(passwd)
    if ctr[char] >= min_o and ctr[char] <= max_o:
        return True

    return False


def is_passwd_valid_2(pos1, pos2, char, passwd) -> bool:
    pos1 -= 1
    pos2 -= 1
    if (passwd[pos1] == char and passwd[pos2] != char) or (passwd[pos1] != char and passwd[pos2] == char):
        return True

    return False


def resolve_day2():
    inputs = load_input_lines(2)
   

    valid_passes = 0
    valid_passes2 = 0
    for line in inputs:
        token1, token2, char, passwd = parse_policy(line)
        # part1
        if is_passwd_valid(token1, token2, char, passwd):
            valid_passes += 1
        # part2
        if is_passwd_valid_2(token1, token2, char, passwd):
            valid_passes2 += 1

    return valid_passes, valid_passes2


def resolve_day3():
    inputs = load_input_lines(3)
    piece_width = len(inputs[0])
    piece_height = len(inputs)

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

            if is_tree(inputs[y][x]):
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
    # print(resolve_day1())
    # print(resolve_day2())
    print(resolve_day3())


if __name__ == "__main__":
    main()
