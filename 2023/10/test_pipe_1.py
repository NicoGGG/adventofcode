import unittest
from pipe_1 import resolve_exercise, get_starting_point, find_next_pipe


class TestPipe(unittest.TestCase):
    def setUp(self):
        file1 = open("file_test_1.txt")
        self.lines1 = file1.read().splitlines()
        file1.close()
        file2 = open("file_test_2.txt")
        self.lines2 = file2.read().splitlines()
        file2.close()

    def test_example_1(self):
        r = resolve_exercise("file_test_1.txt")
        self.assertEqual(4, r)

    def test_example_2(self):
        r = resolve_exercise("file_test_2.txt")
        self.assertEqual(8, r)

    def test_get_starting_point_1(self):
        r = get_starting_point(self.lines1)
        e = (1, 1)
        self.assertEqual(e, r)

    def test_get_starting_point_2(self):
        r = get_starting_point(self.lines2)
        e = (2, 0)
        self.assertEqual(e, r)

    def test_find_first_next_pipe_1_1(self):
        current_position = (1, 1)
        previous_position = None
        r = find_next_pipe(previous_position, current_position, self.lines1)
        e = (1, 2)
        self.assertEqual(e, r)

    def test_find_first_next_pipe_1_2(self):
        current_position = (1, 2)
        previous_position = (1, 1)
        r = find_next_pipe(previous_position, current_position, self.lines1)
        e = (1, 3)
        self.assertEqual(e, r)

    def test_find_first_next_pipe_1_3(self):
        current_position = (1, 3)
        previous_position = (1, 2)
        r = find_next_pipe(previous_position, current_position, self.lines1)
        e = (2, 3)
        self.assertEqual(e, r)

    def test_find_first_next_pipe_2_1(self):
        current_position = (2, 3)
        previous_position = (1, 3)
        r = find_next_pipe(previous_position, current_position, self.lines2)
        e = (2, 4)
        self.assertEqual(e, r)
