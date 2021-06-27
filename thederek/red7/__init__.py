from typing import NamedTuple, List
from enum import IntEnum

class Colour(IntEnum):
    VIOLET = 1
    INGIDO = 2
    BLUE = 3
    GREEN = 4
    YELLOW = 5
    ORANGE = 6
    RED = 7

class Card(NamedTuple):
    number: int
    colour: Colour

    def __repr__(self) -> str:
        return f"{self.colour.name[0].lower()}{self.number}"

class Cards:
    def __init__(self, cards: List[Card]) -> None:
        self._cards: List[Card] = cards

    def __repr__(self) -> str:
        return "".join(repr(card) for card in self._cards)

    def __getitem__(self, key):
        items = self._cards[key]
        if isinstance(items, List):
            return Cards(items)
        
        return items

