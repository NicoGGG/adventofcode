import re


def find_adjacent_numbers_power(l: int, c: int, filepath: str) -> list[int]:
    file = open(filepath, "r")
    lines = file.readlines()
    adjacent_numbers = []
    for i, line in enumerate(lines):
        if i == l - 1 or i == l or i == l + 1:
            iter = re.finditer("\d+", line)
            indices = [m for m in iter]
            adjacent_numbers += [
                m
                for m in indices
                if c + 1 in range(m.span()[0], m.span()[1])
                or c in range(m.span()[0], m.span()[1])
                or c - 1 in range(m.span()[0], m.span()[1])
            ]
    if len(adjacent_numbers) == 2:
        return int(adjacent_numbers[0].group()) * int(adjacent_numbers[1].group())
    return 0


def resolve_exercise(filepath) -> int:
    file = open(filepath, "r")
    lines = file.readlines()
    r = 0
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "*":
                r += find_adjacent_numbers_power(i, j, filepath)

    return r
