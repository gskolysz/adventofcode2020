#!/usr/bin/env python3
from collections import Counter
from pathlib import Path
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def count_group_answers_one_yes(group: list[str]) -> int:
    unique_questions = set()
    for person in group:
        # for question in person:
        unique_questions.update(tuple(person))

    return len(unique_questions)


def count_group_answers_all_yes(group: list[str]) -> int:
    all_yes_questions = 0
    people_count = len(group)
    answers_counter = Counter()
    for person in group:
        answers_counter.update(tuple(person))
    
    for question in answers_counter:
        if answers_counter[question] == people_count:
            all_yes_questions += 1

    return all_yes_questions 


def solve(lines: list[str]) -> tuple[int, int]:
    lines.append("") # so that the loop below can actually execute the function on the last group
    group = []
    sum_of_group_answers_one_yes = 0
    sum_of_group_answers_all_yes = 0
    for line in lines:
        if line == "":
            sum_of_group_answers_one_yes += count_group_answers_one_yes(group)
            sum_of_group_answers_all_yes += count_group_answers_all_yes(group)
            group = []
        else:
            group.append(line)

    return sum_of_group_answers_one_yes, sum_of_group_answers_all_yes


INPUT_S = """\
abc

a
b
c

ab
ac

a
a
a
a

b
"""


def test_solve():
    lines = INPUT_S.split("\n")
    assert solve(lines)[0] == 11
    assert solve(lines)[1] == 6


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
