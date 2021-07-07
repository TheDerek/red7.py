#!/usr/bin/env python3.9

from dataclasses import dataclass

from thederek.red7.player import Player
from thederek.red7.cards import Cards, Card
from thederek.red7.errors import GameLogicError
from thederek.red7.rules import get_rule


@dataclass
class Game:
    deck: Cards
    canvas: Cards
    players: list[Player]
    current_player_idx: int

    def copy(self) -> "Game":
        return Game(
            deck=self.deck.copy(),
            canvas=self.canvas.copy(),
            players=self.players.copy(),
            current_player_idx=self.current_player_idx,
        )

    @property
    def current_player(self) -> Player:
        return self.players[self.current_player_idx]

    @property
    def current_rule(self):
        return get_rule(self.canvas[0].colour)

    @current_player.setter
    def current_player(self, value) -> None:
        self.players[self.current_player_idx] = value

    @staticmethod
    def new(deck: Cards, player_count: int) -> "Game":
        players: list[Player] = []  # (Hand, Palette)

        for position in range(player_count):
            players.append(
                Player(position, hand=deck[:7], palette=deck[7])  # type: ignore
            )

            # Reduce the deck the number of cards we delt to this player (8)
            # type: ignore
            deck = deck[8:]  # type: ignore

        return Game(deck=deck, canvas=Cards([]), players=players, current_player_idx=0)

    def is_current_player_winning(self) -> bool:
        winning_player = self.current_rule(self.players)

        return winning_player == self.current_player

    def play(self, card: Card) -> "Game":
        new_game = self.copy()
        new_game.current_player = new_game.current_player.play(card)

        if not new_game.is_current_player_winning():
            raise GameLogicError("Player is not winning after move")

        return new_game
