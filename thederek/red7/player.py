from dataclasses import dataclass

from thederek.red7.cards import Cards, Card
from thederek.red7.errors import GameLogicError


@dataclass(frozen=True)
class Player:
    position: int
    hand: Cards
    palette: Cards

    def copy(self, args) -> "Player":
        return Player(self.position, self.hand.copy(), self.palette.copy(), **args)

    def play(self, card: Card) -> "Player":
        if card not in self.hand:
            raise GameLogicError("No card in palette")

        return Player(self.position, self.hand - {card}, self.palette | {card})
