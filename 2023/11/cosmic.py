# That was useless in the end after solving part 2 in a more efficient way
def expand(lines: list[str]) -> list[str]:
    insert = False
    for i, line in enumerate(lines):
        if insert:
            lines.insert(i - 1, "." * len(line))
            insert = False
        if any(c != "." for c in line):
            continue
        insert = True
    insert = False
    j = 0
    while j < len(lines[0]):
        if insert:
            for i in range(len(lines)):
                lines[i] = lines[i][:j] + "." + lines[i][j:]
            insert = False
            j += 1
        col = [line[j] for line in lines]
        if any(c != "." for c in col):
            j += 1
            continue
        insert = True
        j += 1
    return lines


def find_empty_space(lines: list[str]) -> tuple[list[int], list[int]]:
    # first list in the tuple are all the empty row, second is the empty col
    empty_space: tuple[list[int], list[int]] = ([], [])
    for i, line in enumerate(lines):
        if all(c == "." for c in line):
            empty_space[0].append(i)
    j = 0
    while j < len(lines[0]):
        col = [line[j] for line in lines]
        if all(c == "." for c in col):
            empty_space[1].append(j)
        j += 1
    return empty_space


def find_galaxies(expanded: list[str]):
    galaxies: list[tuple[int, int]] = []
    for i, line in enumerate(expanded):
        for j, c in enumerate(line):
            if c == "#":
                galaxies.append((i, j))
    return galaxies


def resolve_exercise(filepath: str, empty_multiplier: int = 2):
    file = open(filepath)
    lines = file.read().splitlines()
    file.close()

    galaxies = find_galaxies(lines)
    empty_spaces = find_empty_space(lines)
    r = 0
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            r += abs(galaxies[i][0] - galaxies[j][0]) + abs(
                galaxies[i][1] - galaxies[j][1]
            )
            row_cross = 0
            for empty_row in empty_spaces[0]:
                min_row = min(galaxies[i][0], galaxies[j][0])
                max_row = max(galaxies[i][0], galaxies[j][0])
                if empty_row in range(min_row, max_row):
                    row_cross += 1
            col_cross = 0
            for empty_col in empty_spaces[1]:
                min_col = min(galaxies[i][1], galaxies[j][1])
                max_col = max(galaxies[i][1], galaxies[j][1])
                if empty_col in range(min_col, max_col):
                    col_cross += 1
            r += (col_cross + row_cross) * (empty_multiplier - 1)
    return r
