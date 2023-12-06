def find_winning_combination(time: int, distance: int):
    r = 0
    # prep time * (time - prep time) must be > distance
    for i in range(time):
        if i * (time - i) > distance:
            r += 1
    return r


def find_winning_combination_partial(time: int, distance: int):
    start = 0
    end = 0
    for i in range(time):
        if start == 0 and i * (time - i) > distance:
            start = i
        if end == 0 and (time - i) * i > distance:
            end = time - i
    return end - start + 1


def resolve_exercise(filepath, optim: bool = True):
    input = open(filepath, "r").read().splitlines()
    time = int("".join(input[0].split(":")[1].split()))
    distance = int("".join(input[1].split(":")[1].split()))
    if optim:
        r = find_winning_combination_partial(time, distance)
    else:
        r = find_winning_combination(time, distance)
    return r
