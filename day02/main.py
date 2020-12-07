#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


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


def solve(lines: list[str]) -> tuple[int, int]:
    valid_passes = 0
    valid_passes2 = 0
    for line in lines:
        token1, token2, char, passwd = parse_policy(line)
        # part1
        if is_passwd_valid(token1, token2, char, passwd):
            valid_passes += 1
        # part2
        if is_passwd_valid_2(token1, token2, char, passwd):
            valid_passes2 += 1

    return valid_passes, valid_passes2


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
