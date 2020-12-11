#!/usr/bin/env python3
from pathlib import Path
from typing import Union


MAX_ID = int(pow(2, 7) * pow(2, 3))
MIN_ID = 0

def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return [x.strip() for x in f.readlines()]


def decode_seat(line: str) -> tuple[int, int]:
    numbers_row = []
    numbers_column = []
    row = line[0:7]
    column = line[7:10]
    for char in row:
        if char == "F":
            numbers_row.append("0")
        else:
            numbers_row.append("1")
    for char in column:
        if char == "L":
            numbers_column.append("0")
        else:
            numbers_column.append("1")
    
    dec_row = int("".join(numbers_row), 2)
    dec_col = int("".join(numbers_column), 2)
    return dec_row, dec_col


def find_missing_seat(seats):
    for i in range(min(seats), max(seats)+1):
        if i not in seats:
            return i


def solve(lines: list[str]) -> tuple[int, int]:
    seat_values = []
    for line in lines:
        seat_row, seat_col = decode_seat(line)
        seat_values.append(seat_row * 8 + seat_col)

    max_id = max(seat_values)
    # part2
    missing_seat = find_missing_seat(seat_values)

    return max(seat_values), missing_seat


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
