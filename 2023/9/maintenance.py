def get_differences_from_sequence(sequence: list[int]):
    differences = []
    l = len(sequence)
    for i in range(l - 1):
        differences.append(sequence[i + 1] - sequence[i])
    return differences


def resolve_exercise(filepath: str, reverse: bool = False):
    file = open(filepath, "r")
    lines = file.read().splitlines()
    file.close()
    all_result: int = 0
    for line in lines:
        sequence = list(map(int, line.split()))
        all_sequences: list[int] = [sequence]
        last_differences = get_differences_from_sequence(sequence)
        all_sequences.append(last_differences)
        while any(a != 0 for a in last_differences):
            last_differences = get_differences_from_sequence(last_differences)
            all_sequences.append(last_differences)
        r: list[int] = []
        while len(all_sequences) >= 2:
            if not reverse:
                last = all_sequences.pop()
                to_complete = all_sequences[-1]
                last_n = last.pop()
                complete_n = to_complete[-1]
                next = complete_n + last_n
                all_sequences[-1].append(next)
            else:
                last = all_sequences.pop()
                to_complete = all_sequences[-1]
                last_n = last.pop(0)
                complete_n = to_complete[0]
                next = complete_n - last_n
                all_sequences[-1].insert(0, next)
            r.append(next)
        all_result += r.pop()
    return all_result
