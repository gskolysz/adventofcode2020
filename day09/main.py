#!/usr/bin/env python3
from collections import deque
from pathlib import Path
from typing import Iterable
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [int(x.strip()) for x in f.readlines()]


def check_number_correct(number: int, prev25: Iterable[int]) -> bool:
    for i in prev25:
        wanted = number - i
        others = list(prev25)
        others.remove(i)
        if wanted in others:
            return True

    return False


def find_pair_in_prev25(lines: list[int]) -> int:
    prev25 = deque(lines[:25])
    
    for i in range(25, len(lines)):
        number = lines[i]
        if not check_number_correct(number, prev25):
            return number
        else:
            prev25.popleft()
            prev25.append(number)


def find_contigous_to_sum(lines: list[int], wanted: int) -> Iterable[int]:
    idx = lines.index(wanted)
    for i in range(len(lines)):
        if lines[i] > wanted:
            break

        for j in range(2, idx-i):
            contigous = lines[i:i+j]
            # print(wanted)
            # print(contigous)
            sumc = sum(contigous)
            # print(sumc)
            # print()
            if sumc > wanted:
                break

            if sumc == wanted:
                return contigous


def solve(lines: list[int]) -> tuple[int, int]:
    part1 = find_pair_in_prev25(lines)

    cnums = find_contigous_to_sum(lines, part1)
    part2 = min(cnums) + max(cnums)
    # part2 = None

    return part1, part2



INPUT_S = """\
35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_find_contigous_to_sum():
    lines = INPUT_S.split("\n")
    print(lines)
    lines = [int(x) for x in lines]

    c = find_contigous_to_sum(lines, 127)
    res = min(c) + max(c)
    assert res == 62


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    print("Part two:", solution[1])


if __name__ == "__main__":
    main()
