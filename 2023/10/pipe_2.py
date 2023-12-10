from pipe_1 import find_next_pipe, get_starting_point


def is_inside_loop(
    i: int, j: int, loop_pipes: list[tuple[int, int]], lines: list[str]
) -> int:
    # for all directions, count the number of times the current tile crosses a perpendicular loop tile
    # north
    e = 0
    w = 0
    y = i
    x = j
    while y >= 0:
        # if (y, x) in loop_pipes and lines[y][x] in "LF7J":
        #     r += 0.5
        if (y, x) in loop_pipes and lines[y][x] in "-LFS":
            e += 1
        if (y, x) in loop_pipes and lines[y][x] in "-J7S":
            w += 1
        y -= 1
    if min(e, w) % 2 == 1:
        return 1
    return 0


def count_inside_tiles(loop_pipes: list[tuple[int, int]], lines: list[str]) -> int:
    r = 0
    for i, line in enumerate(lines):
        for j in range(len(line)):
            if (i, j) not in loop_pipes:
                r += is_inside_loop(i, j, loop_pipes, lines)
    return r


def resolve_exercise(filepath: str):
    file = open(filepath, "r")
    lines = file.read().splitlines()
    file.close()
    starting_point = get_starting_point(lines)
    current_position = starting_point
    previous_position = None
    loop_pipes: list[tuple[int, int]] = [starting_point]
    while current_position != None:
        next_position = find_next_pipe(previous_position, current_position, lines)
        previous_position = current_position
        current_position = next_position
        loop_pipes.append(current_position)

    # replace the starting S by the fitting pipe
    x = starting_point[1]
    y = starting_point[0]
    if lines[y][x - 1] in "-FL" and lines[y - 1][x] in "F7|":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "J")
    if lines[y][x - 1] in "-FL" and lines[y][x + 1] in "-J7":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "-")
    if lines[y][x - 1] in "-FL" and lines[y + 1][x] in "JL|":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "7")

    if lines[y - 1][x] in "|F7" and lines[y][x + 1] in "-7J":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "L")
    if lines[y - 1][x] in "|F7" and lines[y + 1][x] in "|JL":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "|")
    if lines[y - 1][x] in "|F7" and lines[y][x - 1] in "-LF":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "J")

    if lines[y][x + 1] in "-J7" and lines[y - 1][x] in "F7|":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "L")
    if lines[y][x + 1] in "-J7" and lines[y][x - 1] in "-FL":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "-")
    if lines[y][x + 1] in "-J7" and lines[y + 1][x] in "LJ|":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "F")

    if lines[y + 1][x] in "|LJ" and lines[y][x + 1] in "-7J":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "F")
    if lines[y + 1][x] in "|LJ" and lines[y - 1][x] in "|F7":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "|")
    if lines[y + 1][x] in "|LJ" and lines[y][x - 1] in "-LF":
        lines[starting_point[0]] = lines[starting_point[0]].replace("S", "7")
    r = count_inside_tiles(loop_pipes, lines)
    return r
