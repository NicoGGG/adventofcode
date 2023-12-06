from wait_for_it_1 import resolve_exercise as resolve_exercise_1
from wait_for_it_2 import resolve_exercise as resolve_exercise_2
import time

if __name__ == "__main__":
    print("Part 1:", resolve_exercise_1("file.txt"))

    start = time.perf_counter()
    print("Part 2:", resolve_exercise_2("file.txt"))
    end = time.perf_counter()
    print(f"Complete range traversal: took {end - start}secs")

    start = time.perf_counter()
    print("Part 2:", resolve_exercise_2("file.txt", False))
    end = time.perf_counter()
    print(f"Partial range traversal: took {end - start}secs")
