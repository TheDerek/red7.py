#!/usr/bin/env python3.9

from typing import List, Union
import itertools
import random
import sqlite3
import random

from thederek.red7.player import Player
from thederek.red7 import Card, Cards, Colour

colour_names = {
    1: "Violet",
    2: "Indigo",
    3: "Blue",
    4: "Green",
    5: "Yellow",
    6: "Orange",
    7: "Red",
}

colour_codes = {value: name[0].lower() for (value, name) in colour_names.items()}


class GameLogicError(RuntimeError):
    pass


class Game:
    @staticmethod
    def _get_deck() -> Cards:
        cards = Cards(
            [
                Card(number, colour)
                for number, colour in itertools.product(range(1, 8), list(Colour))
            ]
        )
        return cards

    @staticmethod
    def new(player_count: int):
        current_position = random.randrange(0, player_count)
        deck: Cards = Game._get_deck()
        players: List[Player] = []  # (Hand, Palette)

        for position in range(player_count):
            players.append(
                Player(position, hand=deck[:7], palette=deck[7])  # type: ignore
            )

            # Reduce the deck the number of cards we delt to this player (8)
            # type: ignore
            deck = deck[8:]  # type: ignore

        return Game(deck, Cards([]), players, current_position)

    def __init__(
        self,
        deck: Cards,
        canvas: Cards,
        players: List[Player],
        current_position: int,
        id_: int = None,
    ) -> None:
        self.deck = deck
        self.canvas = canvas
        self.players = players
        self.current_position = current_position
        self._id = id_

    def create(self, conn: sqlite3.Connection) -> "Game":
        if self._id:
            raise RuntimeError("Game has already been created and written to database")

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO game (current_position, deck, canvas) VALUES (?, ?, ?)",
            [self.current_position, repr(self.deck), ""],
        )

        for player in self.players:
            player.create(cur)

        game_id = cur.execute("select seq from sqlite_sequence where name='game'")
        conn.commit()

        self._id = game_id.fetchone()[0]
        return self

    def copy(self):
        return Game(
            self.deck,
            self.canvas,
            [player.copy() for player in self.players],
            self.current_position,
            self._id,
        )

    @property
    def id(self) -> int:
        if self._id == None:
            raise RuntimeError("Game has not yet been created in the database")
        return self._id

    @property
    def current_player(self) -> Player:
        return self.players[self.current_position]

    def _play(self, card: Card) -> "Game":
        if card not in self.current_player.hand:
            raise GameLogicError(
                f"Player {self.current_player.position} does not have card {card} to play, cards={self.current_player.hand}"
            )

        new_game = self.copy()

    def discard(self, card: Card):
        if card not in self.current_player.hand:
            raise GameLogicError(
                f"Player {self.current_player.position} does not have card {card} to discard"
            )
        pass

    def play_and_discard(self, play_card: Card, discard_card: Card):
        if play_card == discard_card:
            raise GameLogicError("Cannot play and discard the same card")

        self.play(play_card)
        self.discard(discard_card)

    def do_nothing(self):
        pass

    def is_current_player_winning(self):
        pass


def get_name(number: int, colour: int) -> str:
    if colour == 0 or number == 0:
        raise RuntimeError("Invalid card supplied")

    return f"{colour_names[colour]}{number}"


def get_card_names(cards: bytes) -> List[str]:
    card_names: List[str] = []
    for i in range(len(cards) // 2):
        index = i * 2
        number = cards[index]
        colour = cards[index + 1]
        card_names.append(get_name(number, colour))

    return card_names
