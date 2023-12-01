import unittest

from read_calibration import find_combination, where_is_next_digit


class TestReadCalibration(unittest.TestCase):
    def test_example1(self):
        i = "6nineseven9eight3"
        e = 63
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example2(self):
        i = "sevenxgqxtjdjpq3"
        e = 73
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example3(self):
        i = "14gxqgqsqqbxfpxnbccjc33eight"
        e = 18
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example4(self):
        i = "six9mnfjmtsf2kfmznkxntninesevenrpmfjfpgsk"
        e = 67
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example5(self):
        i = "mcrxqxcxgq3eight9"
        e = 39
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example6(self):
        i = "hnmvzknine1"
        e = 91
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example7(self):
        i = "fngf62fourfivetwothree"
        e = 63
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example8(self):
        i = "six"
        e = 66
        r = find_combination(i)
        self.assertEqual(e, r)

    def test_example9(self):
        i1 = "eighthree"
        e1 = 83
        r1 = find_combination(i1)
        self.assertEqual(e1, r1)

    def test_example10(self):
        i2 = "sevenine"
        e2 = 79
        r2 = find_combination(i2)
        self.assertEqual(e2, r2)

    """
    two1nine: 29
    eightwothree: 83
    abcone2threexyz: 13
    xtwone3four: 24
    4nineeightseven2: 42
    zoneight234: 14
    7pqrstsixteen: 76
    """

    def test_examples_question(self):
        i1 = "two1nine"
        i2 = "eightwothree"
        i3 = "abcone2threexyz"
        i4 = "xtwone3four"
        i5 = "4nineeightseven2"
        i6 = "zoneight234"
        i7 = "7pqrstsixteen"
        e1 = 29
        e2 = 83
        e3 = 13
        e4 = 24
        e5 = 42
        e6 = 14
        e7 = 76
        r1 = find_combination(i1)
        r2 = find_combination(i2)
        r3 = find_combination(i3)
        r4 = find_combination(i4)
        r5 = find_combination(i5)
        r6 = find_combination(i6)
        r7 = find_combination(i7)
        self.assertEqual(e1, r1)
        self.assertEqual(e2, r2)
        self.assertEqual(e3, r3)
        self.assertEqual(e4, r4)
        self.assertEqual(e5, r5)
        self.assertEqual(e6, r6)
        self.assertEqual(e7, r7)


class TestIsDigit(unittest.TestCase):
    def test_example1(self):
        i = "eight"
        e = (0, 4)
        r = where_is_next_digit(0, i)
        self.assertEqual(e, r)

    def test_example2(self):
        i = "eighw"
        e = None
        r = where_is_next_digit(0, i)
        self.assertEqual(e, r)

    def test_example3(self):
        i = "2sadij"
        e = (0, 0)
        r = where_is_next_digit(0, i)
        self.assertEqual(e, r)

    def test_example4(self):
        i = "2"
        e = (0, 0)
        r = where_is_next_digit(0, i)
        self.assertEqual(e, r)

    def test_example5(self):
        i = "asdqweight"
        e = (5, 9)
        r = where_is_next_digit(0, i)
        self.assertEqual(e, r)
