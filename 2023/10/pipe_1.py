import re


def find_next_pipe(
    previous_position: tuple[int, int],
    current_position: tuple[int, int],
    lines: list[str],
):
    current_pipe = lines[current_position[0]][current_position[1]]
    x = current_position[1]
    y = current_position[0]
    north_pipes = "|F7"
    east_pipes = "-J7"
    south_pipes = "|JL"
    west_pipes = "-LF"
    if current_pipe == "S":
        # find the first connected pipe, starting north and searching clockwise
        if y - 1 >= 0 and lines[y - 1][x] in north_pipes:
            return (y - 1, x)
        if x + 1 < len(lines[0]) and lines[y][x + 1] in east_pipes:
            return (y, x + 1)
        if y + 1 < len(lines) and lines[y + 1][x] in south_pipes:
            return (y + 1, x)
        if x - 1 >= 0 and lines[y][x - 1] in west_pipes:
            return (y, x - 1)
    elif current_pipe == "|":
        # north
        if (
            y - 1 >= 0
            and lines[y - 1][x] in north_pipes
            and (y - 1, x) != previous_position
        ):
            return (y - 1, x)
        # south
        if (
            y + 1 < len(lines)
            and lines[y + 1][x] in south_pipes
            and (y + 1, x) != previous_position
        ):
            return (y + 1, x)
    elif current_pipe == "-":
        # east
        if (
            x + 1 < len(lines[0])
            and lines[y][x + 1] in east_pipes
            and (y, x + 1) != previous_position
        ):
            return (y, x + 1)
        # west
        if (
            x - 1 >= 0
            and lines[y][x - 1] in west_pipes
            and (y, x - 1) != previous_position
        ):
            return (y, x - 1)
    elif current_pipe == "J":
        # north
        if (
            y - 1 >= 0
            and lines[y - 1][x] in north_pipes
            and (y - 1, x) != previous_position
        ):
            return (y - 1, x)
        # west
        if (
            x - 1 >= 0
            and lines[y][x - 1] in west_pipes
            and (y, x - 1) != previous_position
        ):
            return (y, x - 1)
    elif current_pipe == "F":
        # east
        if (
            x + 1 < len(lines[0])
            and lines[y][x + 1] in east_pipes
            and (y, x + 1) != previous_position
        ):
            return (y, x + 1)
        # south
        if (
            y + 1 < len(lines)
            and lines[y + 1][x] in south_pipes
            and (y + 1, x) != previous_position
        ):
            return (y + 1, x)
    elif current_pipe == "L":
        # north
        if (
            y - 1 >= 0
            and lines[y - 1][x] in north_pipes
            and (y - 1, x) != previous_position
        ):
            return (y - 1, x)
        # east
        if (
            x + 1 < len(lines[0])
            and lines[y][x + 1] in east_pipes
            and (y, x + 1) != previous_position
        ):
            return (y, x + 1)
    elif current_pipe == "7":
        # south
        if (
            y + 1 < len(lines)
            and lines[y + 1][x] in south_pipes
            and (y + 1, x) != previous_position
        ):
            return (y + 1, x)
        # west
        if (
            x - 1 >= 0
            and lines[y][x - 1] in west_pipes
            and (y, x - 1) != previous_position
        ):
            return (y, x - 1)


def get_starting_point(lines: list[str]):
    for i, line in enumerate(lines):
        if "S" in line:
            return (i, line.find("S"))


def resolve_exercise(filepath: str):
    file = open(filepath, "r")
    lines = file.read().splitlines()
    file.close()
    starting_point = get_starting_point(lines)
    current_position = starting_point
    previous_position = None
    i = 0
    while i == 0 or current_position != None:
        next_position = find_next_pipe(previous_position, current_position, lines)
        previous_position = current_position
        current_position = next_position
        i += 1
    return i // 2
