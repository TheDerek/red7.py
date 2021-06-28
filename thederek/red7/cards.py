from typing import NamedTuple
from enum import IntEnum
import itertools


class Colour(IntEnum):
    VIOLET = 1
    INGIDO = 2
    BLUE = 3
    GREEN = 4
    YELLOW = 5
    ORANGE = 6
    RED = 7


COLOUR_MAPPINGS: dict[str, Colour] = {
    "v": Colour.VIOLET,
    "i": Colour.INGIDO,
    "b": Colour.BLUE,
    "g": Colour.GREEN,
    "y": Colour.YELLOW,
    "o": Colour.ORANGE,
    "r": Colour.RED,
}


class Card(NamedTuple):
    number: int
    colour: Colour

    def __repr__(self) -> str:
        return f"{self.colour.name[0].lower()}{self.number}"


Cards = list[Card]


def get_deck() -> Cards:
    cards = Cards(
        [
            Card(number, colour)
            for number, colour in itertools.product(range(1, 8), list(Colour))
        ]
    )
    return cards


def get_cards(source: str) -> list[Card]:
    cards = []

    if len(source) % 2 != 0:
        raise RuntimeError("Invalid card string provided")

    for i in range(0, len(source) // 2):
        colour = source[i * 2]
        number = source[(i * 2) + 1]
        cards.append(Card(int(number), COLOUR_MAPPINGS[colour]))

    return cards
