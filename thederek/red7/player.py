from dataclasses import dataclass

from thederek.red7.cards import Cards, Card
from thederek.red7.errors import GameLogicError


@dataclass
class Player:
    position: int
    hand: Cards
    palette: Cards

    def copy(self) -> "Player":
        return Player(self.position, self.hand.copy(), self.palette.copy())

    def play(self, card: Card) -> "Player":
        if card not in self.hand:
            raise GameLogicError("No card in palette")

        new_player = self.copy()
        new_player.palette.append(new_player.hand.pop())
        return new_player
