import unittest
from cosmic import resolve_exercise, expand, find_galaxies, find_empty_space


class TestPipe(unittest.TestCase):
    def setUp(self):
        file1 = open("file_test.txt")
        self.lines1 = file1.read().splitlines()
        file1.close()

    def test_example_1(self):
        r = resolve_exercise("file_test.txt")
        self.assertEqual(374, r)

    def test_example_2(self):
        r = resolve_exercise("file_test.txt", 10)
        self.assertEqual(1030, r)

    def test_example_3(self):
        r = resolve_exercise("file_test.txt", 100)
        self.assertEqual(8410, r)

    def test_expand_1(self):
        r = expand(self.lines1)
        self.assertEqual(13, len(r[0]))
        self.assertEqual(12, len(r))
        self.assertEqual("....#........", r[0])
        self.assertEqual(".............", r[3])
        self.assertEqual(".............", r[4])
        self.assertEqual("#....#.......", r[11])

    def test_find_galaxies_1(self):
        lines = expand(self.lines1)
        r = find_galaxies(lines)
        self.assertEqual(9, len(r))
        self.assertTrue((0, 4) in r)
        self.assertTrue((1, 9) in r)
        self.assertTrue((2, 0) in r)
        self.assertTrue((5, 8) in r)
        self.assertTrue((6, 1) in r)
        self.assertTrue((7, 12) in r)
        self.assertTrue((10, 9) in r)
        self.assertTrue((11, 0) in r)
        self.assertTrue((11, 5) in r)

    def test_find_empty_space(self):
        r = find_empty_space(self.lines1)
        self.assertEqual([3, 7], r[0])
        self.assertEqual([2, 5, 8], r[1])
