import unittest
from wasteland_1 import resolve_exercise as resolve_exercise_1
from wasteland_2 import resolve_exercise as resolve_exercise_2


class TestWastelandPart1(unittest.TestCase):
    def test_wasteland_example_1(self):
        filepath = "file_test_1.txt"
        r = resolve_exercise_1(filepath)
        self.assertEqual(2, r)

    def test_wasteland_example_2(self):
        filepath = "file_test_2.txt"
        r = resolve_exercise_1(filepath)
        self.assertEqual(6, r)


class TestWastelandPart2(unittest.TestCase):
    def test_wasteland_example_1(self):
        filepath = "file_test_3.txt"
        r = resolve_exercise_2(filepath)
        self.assertEqual(6, r)
