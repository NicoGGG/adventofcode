import unittest
from maintenance import resolve_exercise, get_differences_from_sequence


class TestMaintenance(unittest.TestCase):
    def test_example_1(self):
        r = resolve_exercise("file_test.txt")
        self.assertEqual(114, r)

    def test_example_2(self):
        r = resolve_exercise("file_test.txt", True)
        self.assertEqual(2, r)

    def test_get_difference_from_sequence(self):
        i = [3, 3, 3, 3]
        e = [0, 0, 0]
        r = get_differences_from_sequence(i)
        self.assertEqual(e, r)
