def find_winning_combination(time: int, distance: int):
    r = 0
    # prep time * (time - prep time) must be > distance
    for i in range(time):
        if i * (time - i) > distance:
            r += 1
    return r


def resolve_exercise(filepath):
    input = open(filepath, "r").read().splitlines()
    times = list(map(int, input[0].split(":")[1].split()))
    distances = list(map(int, input[1].split(":")[1].split()))
    r = 1
    for i, time in enumerate(times):
        r *= find_winning_combination(time, distances[i])
    return r
