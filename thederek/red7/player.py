import sqlite3

from thederek.red7 import Cards


class Player:
    def __init__(self, position: int, hand: Cards, palette: Cards):
        self.position = position
        self.hand: Cards = hand
        self.palette: Cards = palette

    def create(self, cursor: sqlite3.Cursor):
        cursor.execute(
            "INSERT INTO player (game_id, position, hand, palette) VALUES (?, (select seq from sqlite_sequence where name='game'), ?, ?)",
            [self.position, repr(self.hand), repr(self.palette)],
        )
