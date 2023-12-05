def solve_cards(lines: list[str], start, end, current_score: int = 1) -> int:
    if len(lines) == 0:
        return current_score
    sub_lines = lines[start:end]
    for i, line in enumerate(sub_lines):
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
            current_score = solve_cards(
                lines, i + start + 1, i + start + win + 1, current_score + 1
            )
        else:
            current_score += 1
    return current_score


def resolve_exercise(filepath: str):
    file = open(filepath)
    lines = file.read().splitlines()
    r = solve_cards(lines, 0, len(lines) - 1)
    file.close()
    return r
