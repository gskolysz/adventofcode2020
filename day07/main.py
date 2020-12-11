#!/usr/bin/env python3
from pathlib import Path
from typing import Union


BAG_NAME = "shiny gold"


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def parse_rules(lines: list[str]) -> dict[str, dict[str, int]]:
    rules = dict()
    for line in lines:
        line = line.removesuffix(".")
        # print(line)
        outer_bag, inner_bags = line.split("contain")
        outer_bag = outer_bag.strip().removesuffix(" bags")
        rules.update({outer_bag: {}})
        inner_bags = inner_bags.strip().split(", ")
        for i_b in inner_bags:
            if i_b == "no other bags":
                rules[outer_bag] = {}
            else:
                i_b_count = i_b[0]
                i_b_name = i_b[2:]
                rules.setdefault(outer_bag, {}).update(
                    {i_b_name.removesuffix("s").removesuffix(" bag"): i_b_count}
                )

    return rules


def how_many_can_carry_my_bag(rules, bag, all_bags: set[str]) -> None:
    for outer_bag, inner_bags in rules.items():
        if bag in list(inner_bags.keys()):
            # print(f"{bag} in {outer_bag})
            all_bags.add(outer_bag)
            how_many_can_carry_my_bag(rules, outer_bag, all_bags)


def how_many_does_my_bag_carry(rules, bag, total_bags) -> None:
    for inner_bag, count in rules[bag].items():
        # print(f"In {bag} I have {count} {inner_bag} bags")
        int_count = int(count)
        total_bags.append(int_count)
        for _ in range(int_count):
            how_many_does_my_bag_carry(rules, inner_bag, total_bags)


def solve(lines: list[str]) -> tuple[int, int]:
    rules = parse_rules(lines)
    all_bags = set()
    how_many_can_carry_my_bag(rules, BAG_NAME, all_bags)
    part1 = len(all_bags)
    total_bags = []
    how_many_does_my_bag_carry(rules, BAG_NAME, total_bags)
    part2 = sum(total_bags)
    return part1, part2


INPUT_S = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.\
"""


def test_solve():
    lines = INPUT_S.split("\n")
    p1, p2 = solve(lines)
    assert p1 == 4
    assert p2 == 32


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
