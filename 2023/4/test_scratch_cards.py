import unittest
from scratch_cards_1 import resolve_exercise as resolve_exercise_1
from scratch_cards_2 import resolve_exercise as resolve_exercise_2


class TestScratchCard(unittest.TestCase):
    def test_example_input_part_1(self):
        filepath = "file_test.txt"
        r = resolve_exercise_1(filepath)
        self.assertEqual(13, r)

    def test_example_input_part_2(self):
        filepath = "file_test.txt"
        r = resolve_exercise_2(filepath)
        self.assertEqual(30, r)
