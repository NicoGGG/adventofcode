def find_winning_combination(time: int, distance: int):
    r = 0
    # prep time * (time - prep time) must be > distance
    for i in range(time):
        if i * (time - i) > distance:
            r += 1
    return r


def resolve_exercise(filepath):
    input = open(filepath, "r").read().splitlines()
    time = int("".join(input[0].split(":")[1].split()))
    distance = int("".join(input[1].split(":")[1].split()))
    print(time)
    print(distance)
    r = find_winning_combination(time, distance)
    # for i, time in enumerate(times):
    #     r *= find_winning_combination(time, distances[i])
    return r
