from __future__ import annotations
from enum import Enum
from functools import total_ordering


@total_ordering
class HandType(Enum):
    FIVE_OF_KIND = 6
    FOUR_OF_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_KIND = 3
    TWO_PAIR = 2
    PAIR = 1
    HIGH_CARD = 0

    def __eq__(self, other: HandType) -> bool:
        return self.value == other.value

    def __lt__(self, other: HandType) -> bool:
        return self.value < other.value


@total_ordering
class Card:
    def __init__(self, card: str):
        self.card = self.convert_str_to_card(card)

    def convert_str_to_card(self, card: str):
        if card == "T":
            return 10
        if card == "J":
            return 1
        if card == "Q":
            return 12
        if card == "K":
            return 13
        if card == "A":
            return 14
        # We assume the card is valid
        return int(card)

    def __eq__(self, other: Card) -> bool:
        return self.card == other.card

    def __lt__(self, other: Card) -> bool:
        return self.card < other.card


@total_ordering
class Hand:
    def __init__(self, hand: str, bid: int):
        self.hand: list[Card] = []
        self.bid = bid
        self.type = None
        self.set_type(hand)
        self.set_hand(hand)

    def set_hand(self, hand):
        for card in hand:
            new_card = Card(card)
            self.hand.append(new_card)

    def set_type(self, hand: str):
        h = sorted(hand)
        trips = False
        pairs: set[str] = set()
        jokers = h.count("J")
        while "J" in h:
            h.remove("J")
        for card in h:
            if h.count(card) == 5:
                self.type = HandType.FIVE_OF_KIND
                return
            if h.count(card) == 4:
                if jokers == 1:
                    self.type = HandType.FIVE_OF_KIND
                    return
                self.type = HandType.FOUR_OF_KIND
                return
            if h.count(card) == 3:
                if jokers == 1:
                    self.type = HandType.FOUR_OF_KIND
                    return
                if jokers == 2:
                    self.type = HandType.FIVE_OF_KIND
                    return
                trips = True
            if h.count(card) == 2:
                if jokers == 2:
                    self.type = HandType.FOUR_OF_KIND
                    return
                elif jokers == 3:
                    self.type = HandType.FIVE_OF_KIND
                    return
                pairs.add(card)

        if trips and pairs:
            self.type = HandType.FULL_HOUSE
            return
        elif trips:
            self.type = HandType.THREE_OF_KIND
            return
        if len(pairs):
            if len(pairs) == 2:
                if jokers:
                    self.type = HandType.FULL_HOUSE
                else:
                    self.type = HandType.TWO_PAIR
            else:
                if jokers == 1:
                    self.type = HandType.THREE_OF_KIND
                elif jokers == 2:
                    self.type = HandType.FOUR_OF_KIND
                elif jokers == 3:
                    self.type = HandType.FIVE_OF_KIND
                else:
                    self.type = HandType.PAIR
            return
        if jokers == 5:
            self.type = HandType.FIVE_OF_KIND
            return
        if jokers == 1:
            self.type = HandType.PAIR
        elif jokers == 2:
            self.type = HandType.THREE_OF_KIND
        elif jokers == 3:
            self.type = HandType.FOUR_OF_KIND
        elif jokers == 4:
            self.type = HandType.FIVE_OF_KIND
        else:
            self.type = HandType.HIGH_CARD

    def __eq__(self, other: Hand) -> bool:
        if self.type > other.type:
            return False
        if self.type < other.type:
            return False
        for i in range(5):
            if self.hand[i] > other.hand[i]:
                return False
            if self.hand[i] < other.hand[i]:
                return False
        return True

    def __lt__(self, other: Hand) -> bool:
        if self.type > other.type:
            return False
        if self.type < other.type:
            return True
        for i in range(5):
            if self.hand[i] > other.hand[i]:
                return False
            if self.hand[i] < other.hand[i]:
                return True
        return False


def resolve_exercise(filepath: str):
    file = open(filepath, "r")
    lines = file.read().splitlines()
    file.close()
    hands: list[Hand] = []
    for line in lines:
        # We assume all input data from the puzzle is valid
        hands.append(Hand(line.split()[0], int(line.split()[1])))
    sorted_hands = sorted(hands)
    r = 0
    for i, hand in enumerate(sorted_hands):
        r += hand.bid * (i + 1)
    lines
    return r
