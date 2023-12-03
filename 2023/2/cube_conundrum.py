import re


# Use this function in resolve_exercise(filepath) for part 1
def get_game_id(line: str):
    data = line.split(":")
    metadata = data[0]
    id = int(metadata.split(" ")[1].strip())
    draws = re.split(",|;", data[1])
    for draw in draws:
        draw = draw.strip("")
        value, color = draw.split()
        if color == "red" and int(value) > 12:
            return 0
        if color == "green" and int(value) > 13:
            return 0
        if color == "blue" and int(value) > 14:
            return 0
    return id


# Use this function in resolve_exercise(filepath) for part 2
def get_game_power_set(line: str):
    data = line.split(":")
    draws = re.split(",|;", data[1])
    min_blue = 1
    min_red = 1
    min_green = 1
    for draw in draws:
        draw = draw.strip("")
        value, color = draw.split()
        v = int(value)
        if color == "red":
            if v > min_red:
                min_red = v
        if color == "green":
            if v > min_green:
                min_green = v
        if color == "blue":
            if v > min_blue:
                min_blue = v
    return min_blue * min_green * min_red


def resolve_exercise(filepath) -> int:
    file = open(filepath, "r")
    lines = file.readlines()
    r = 0
    for line in lines:
        v = get_game_power_set(line)
        r += v
    return r
