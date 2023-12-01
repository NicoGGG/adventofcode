digits = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]


def digit_to_numeric(s: str) -> str:
    if s not in digits:
        raise ValueError("Not a valid digit")
    if s == "one":
        return "1"
    if s == "two":
        return "2"
    if s == "three":
        return "3"
    if s == "four":
        return "4"
    if s == "five":
        return "5"
    if s == "six":
        return "6"
    if s == "seven":
        return "7"
    if s == "eight":
        return "8"
    if s == "nine":
        return "9"
    return s


def where_is_next_digit(start: int, s: str) -> (int, int):
    """
    Returns a int tupple that represent the index of the start and the end of the digit

    Example: s = "eight" -> (0,4)
             s = "2ec" -> (0,0)
             s = "dqwdeight" -> (4, 8)
    """
    if s == "":
        return None
    for n in digits:
        if s.startswith(n):
            return (start, start + len(n) - 1)
    start += 1
    return where_is_next_digit(start, s[1:])


def find_combination(line: str) -> int:
    first = None
    last = None
    while line != "":
        r = where_is_next_digit(0, line)
        if r is None:
            break
        start, end = r
        digit = digit_to_numeric(line[start : end + 1])
        if first is None:
            first = digit
        last = digit
        # For the edge cases like "sevenine", don't skip the last letter of the digit if it is alphabetical
        # Thanks u/Zefick for the tip
        if start != end:
            line = line[end:]
        else:
            line = line[end + 1 :]
    return int(first + last)


def read_calibration_from_file(filename) -> int:
    file = open(filename, "r")
    lines = file.readlines()
    r = 0
    for line in lines:
        v = find_combination(line)
        r += v
    return r
