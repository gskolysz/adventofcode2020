#!/usr/bin/env python3
import re
from pathlib import Path
from typing import Union


REQUIRED_FIELDS = (
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid"
)


def load_input_lines() -> list[any]:
    full_path = Path(__file__).resolve().parent / "input.txt"
    with open(full_path) as f:
        return f.read()


def validate_field(key, val) -> bool:
    val = str(val)
    if key == "byr":
        if len(val) != 4:
            return False
        if int(val) > 2002 or int(val) < 1920:
            return False
    elif key == "iyr":
        if len(val) != 4:
            return False
        if int(val) > 2020 or int(val) < 2010:
            return False
    elif key == "eyr":
        if len(val) != 4:
            return False
        if int(val) > 2030 or int(val) < 2020:
            return False

    elif key == "hgt":
        if not (val.endswith("cm") or val.endswith("in")):
            return False
        suffix = val[-2:]
        height_n = int(val[0:len(val)-2])
        if suffix == "cm" and (height_n < 150 or height_n > 193):
            return False
        elif suffix == "in" and (height_n < 59 or height_n > 76):
            return False

    elif key == "hcl":
        hex_re = r'^#([0-9a-f]{6})$'
        if not re.match(hex_re, val):
            return False

    elif key == "ecl":
        allowed_eyes = ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")
        if val not in allowed_eyes:
            return False
    
    elif key == "pid":
        pid_re = r'^([0-9]{9})$'
        if not re.match(pid_re, val):
            return False

    return True


def solve(lines: list[str]) -> tuple[int, int]:
    passports = lines.split("\n\n")
    valid_passports = 0
    for passport in passports:
        keys_in_pass = []
        passport = passport.strip("\n")
        passport_replaced = passport.replace("\n", " ")
        fields = passport_replaced.split(" ")
        for field in fields:              
            key, val = field.split(":")
            keys_in_pass.append(key)
            # part 2, comment for part 1
            if not validate_field(key, val):
                break

        if all(rf in keys_in_pass for rf in REQUIRED_FIELDS):
            valid_passports += 1

    return valid_passports,


def main():
    solution = solve(load_input_lines())
    print("Part one:", solution[0])
    try:
        print("Part two:", solution[1])
    except IndexError:
        print("Part two not done yet :)")
    

if __name__ == "__main__":
    main()
