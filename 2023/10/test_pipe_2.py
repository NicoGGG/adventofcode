import unittest
from pipe_2 import resolve_exercise, is_inside_loop
from pipe_1 import get_starting_point, find_next_pipe


class TestPipe(unittest.TestCase):
    def setUp(self):
        # File 2
        file1 = open("file_test_2_1.txt")
        self.lines1 = file1.read().splitlines()
        file1.close()
        starting_point = get_starting_point(self.lines1)
        current_position = starting_point
        previous_position = None
        self.loop_pipes1: list[tuple[int, int]] = [starting_point]
        while current_position != None:
            next_position = find_next_pipe(
                previous_position, current_position, self.lines1
            )
            previous_position = current_position
            current_position = next_position
            self.loop_pipes1.append(current_position)
        # File 2
        file2 = open("file_test_2_2.txt")
        self.lines2 = file2.read().splitlines()
        file2.close()
        starting_point = get_starting_point(self.lines2)
        current_position = starting_point
        previous_position = None
        self.loop_pipes2: list[tuple[int, int]] = [starting_point]
        while current_position != None:
            next_position = find_next_pipe(
                previous_position, current_position, self.lines2
            )
            previous_position = current_position
            current_position = next_position
            self.loop_pipes2.append(current_position)

        # File 3
        file3 = open("file_test_2_2.txt")
        self.lines3 = file3.read().splitlines()
        file3.close()
        starting_point = get_starting_point(self.lines3)
        current_position = starting_point
        previous_position = None
        self.loop_pipes3: list[tuple[int, int]] = [starting_point]
        while current_position != None:
            next_position = find_next_pipe(
                previous_position, current_position, self.lines3
            )
            previous_position = current_position
            current_position = next_position
            self.loop_pipes3.append(current_position)

    def test_example_1(self):
        r = resolve_exercise("file_test_2_1.txt")
        self.assertEqual(4, r)

    def test_example_2(self):
        r = resolve_exercise("file_test_2_2.txt")
        self.assertEqual(8, r)

    def test_example_3(self):
        r = resolve_exercise("file_test_2_3.txt")
        self.assertEqual(10, r)

    def test_is_inside_loop_1_1(self):
        r = is_inside_loop(6, 2, self.loop_pipes1, self.lines1)
        e = 1
        self.assertEqual(e, r)

    def test_is_inside_loop_1_2(self):
        r = is_inside_loop(3, 3, self.loop_pipes1, self.lines1)
        e = 0
        self.assertEqual(e, r)

    def test_is_inside_loop_1_3(self):
        r = is_inside_loop(5, 5, self.loop_pipes1, self.lines1)
        e = 0
        self.assertEqual(e, r)

    def test_is_inside_loop_1_4(self):
        r = is_inside_loop(4, 6, self.loop_pipes1, self.lines1)
        e = 0
        self.assertEqual(e, r)

    def test_is_inside_loop_2_1(self):
        r = is_inside_loop(6, 6, self.loop_pipes2, self.lines2)
        e = 1
        self.assertEqual(e, r)
