import unittest
from wait_for_it_1 import (
    resolve_exercise as resolve_exercise_1,
    find_winning_combination,
)
from wait_for_it_2 import (
    resolve_exercise as resolve_exercise_2,
    find_winning_combination_partial,
)


class TestWaitForIt(unittest.TestCase):
    def test_example_input_part_1(self):
        filepath = "file_test.txt"
        r = resolve_exercise_1(filepath)
        e = 288
        self.assertEqual(e, r)

    def test_example_input_part_2(self):
        filepath = "file_test.txt"
        r = resolve_exercise_2(filepath)
        e = 71503
        self.assertEqual(e, r)

    def test_find_combination_1(self):
        time = 7
        distance = 9
        e = 4
        r = find_winning_combination(time, distance)
        self.assertEqual(e, r)

    def test_find_combination_2(self):
        time = 71530
        distance = 940200
        e = 71503
        r = find_winning_combination_partial(time, distance)
        self.assertEqual(e, r)
