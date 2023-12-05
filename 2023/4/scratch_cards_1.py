def resolve_exercise(filepath):
    file = open(filepath, "r")
    lines = file.readlines()
    r = 0
    for line in lines:
        a = line.split("|")
        winning_numbers = a[0].split(":")[1].strip().split()
        winning_numbers = list(map(int, winning_numbers))
        draw_numbers = a[1].strip().split()
        draw_numbers = list(map(int, draw_numbers))
        win = 0
        for d in draw_numbers:
            if d in winning_numbers:
                win += 1
        if win:
            r += 2 ** (win - 1)
    return r
