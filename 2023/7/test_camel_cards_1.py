import unittest
from camel_cards_1 import Hand, Card, HandType, resolve_exercise as resolve_exercise_1


class TestCamelCard(unittest.TestCase):
    def test_camel_card_example_1(self):
        filepath = "file_test.txt"
        r = resolve_exercise_1(filepath)
        self.assertEqual(6440, r)


class TestHandClass(unittest.TestCase):
    def test_hand_init(self):
        hand1 = "32T4K"
        hand2 = "T55J5"
        hand3 = "KKKKK"
        hand4 = "KTJJT"
        hand5 = "QQQQA"
        hand6 = "KKJKJ"
        hand7 = "KKT98"

        h1 = Hand(hand1, 10)
        h2 = Hand(hand2, 10)
        h3 = Hand(hand3, 10)
        h4 = Hand(hand4, 10)
        h5 = Hand(hand5, 10)
        h6 = Hand(hand6, 10)
        h7 = Hand(hand7, 10)
        self.assertEqual(HandType.FIVE_OF_KIND, h3.type)
        self.assertEqual(HandType.FOUR_OF_KIND, h5.type)
        self.assertEqual(HandType.FULL_HOUSE, h6.type)
        self.assertEqual(HandType.THREE_OF_KIND, h2.type)
        self.assertEqual(HandType.TWO_PAIR, h4.type)
        self.assertEqual(HandType.PAIR, h7.type)
        self.assertEqual(HandType.HIGH_CARD, h1.type)

    def test_hand_eq(self):
        hand1 = "32T4K"
        hand2 = "T55J5"
        hand3 = "T55J5"
        h1 = Hand(hand1, 10)
        h2 = Hand(hand2, 10)
        h3 = Hand(hand3, 10)
        self.assertFalse(h1 == h2)
        self.assertFalse(h1 == h3)
        self.assertTrue(h2 == h3)

    def test_hand_lt(self):
        hand1 = "32KKK"
        hand2 = "T55J5"
        hand3 = "QQQQA"
        h1 = Hand(hand1, 10)
        h2 = Hand(hand2, 10)
        h3 = Hand(hand3, 10)
        self.assertTrue(h1 < h2)
        self.assertTrue(h1 < h3)
        self.assertTrue(h2 < h3)

    def test_hand_gt(self):
        hand1 = "32KKK"
        hand2 = "T55J5"
        hand3 = "QQQQA"
        h1 = Hand(hand1, 10)
        h2 = Hand(hand2, 10)
        h3 = Hand(hand3, 10)
        self.assertFalse(h1 > h2)
        self.assertFalse(h1 > h3)
        self.assertFalse(h2 > h3)
