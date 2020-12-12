#!/usr/bin/env python3
from pathlib import Path
from typing import Union


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def execute_instruction(line: str):
    next_line = 1
    next_acc = 0
    instr, val = line.split(" ")
    val = int(val)
    if instr == "acc":
        next_acc = val
    elif instr == "jmp":
        next_line = val
    
    return next_line, next_acc


def execute_looped_program(lines: list[str]):
    visited = []
    next_line = 0
    acc = 0
    while next_line not in visited:
        # print(f"Already visited: {sorted(visited)}")
        visited.append(next_line)
        # print(f"Line at index {next_line}: {lines[next_line]}")
        # print(f"Current acc value: {acc}")
        add_lines, add_acc = execute_instruction(lines[next_line])
        next_line += add_lines
        acc += add_acc
        # print(f"Next line to visit: {next_line}")

    return acc


class ProgramLoopException(Exception):
    pass


def execute_program_break_on_loop(lines: list[str]):
    visited = []
    next_line = 0
    acc = 0
    while next_line != len(lines):
        visited.append(next_line)
        add_lines, add_acc = execute_instruction(lines[next_line])
        next_line += add_lines
        acc += add_acc
        if next_line in visited:
            raise ProgramLoopException

    return acc

def solve(lines: list[str]) -> tuple[int, int]:
    part1 = execute_looped_program(lines)

    for idx, line in enumerate(lines):
        if line.startswith("jmp"):
            new_program = lines.copy()
            new_program[idx] = line.replace("jmp", "nop")
        elif line.startswith("nop"):
            new_program = lines.copy()
            new_program[idx] = line.replace("nop", "jmp")
        else:
            continue

        try:
            part2 = execute_program_break_on_loop(new_program)
            # print("Found it!")
            break
        except ProgramLoopException:
            # print("Replaced, but the program is still looped :(")
            continue

    return part1, part2

def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    print("Part two:", solution[1])


if __name__ == "__main__":
    main()
