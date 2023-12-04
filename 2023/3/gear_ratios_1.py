symbols = "%$&*/-=+_"


def find_symbol(s: str) -> bool:
    return any(is_symbol(c) for c in s)


def is_symbol(c: str) -> bool:
    return not c.isdigit() and not c == "." and not c.isspace()


def find_adjacent_symbol(l: int, start_number: int, end_number: int, filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    for i, line in enumerate(lines):
        if i == l - 1 or i == l or i == l + 1:
            start = start_number - 1 if start_number > 0 else 0
            end = end_number + 1 if end_number < len(line) - 1 else end_number
            if find_symbol(line[start : end + 1]):
                return True
    return False


def resolve_exercise(filepath) -> int:
    file = open(filepath, "r")
    lines = file.readlines()
    r = 0
    for i, line in enumerate(lines):
        start_number = -1
        end_number = -1
        for j, c in enumerate(line):
            if c.isdigit():
                if start_number == -1:
                    start_number = j
            else:
                if start_number != -1:
                    end_number = j - 1
                    if find_adjacent_symbol(i, start_number, end_number, filepath):
                        number = int(line[start_number : end_number + 1])
                        r += number
                    start_number = -1
                    end_number = -1
    return r
