#!/usr/bin/env python3.9

from typing import List, Tuple
import secrets
import datetime
import itertools
import random
import sqlite3
import random

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


class Game:
    @staticmethod
    def _get_deck() -> str:
        cards = ""
        for colour, number in itertools.product(
            random.sample(list(colour_codes.values()), 7), random.sample(range(1, 8), 7)
        ):
            cards += f"{colour}{number}"

        return cards

    def __init__(self, conn: sqlite3.Connection, player_count: int) -> None:
        self.current_position = random.randrange(0, player_count)
        deck: str = Game._get_deck()
        players: List[Tuple[str, str]] = []  # (Hand, Palette)

        for _ in range(player_count):
            # Two characters for every card so we need to double the hand count of 7
            hand = deck[:14]
            palette = deck[14:16]
            players.append((hand, palette))
            deck = deck[16:]

        cur = conn.cursor()
        cur.execute(
            "INSERT INTO game (current_position, deck, canvas) VALUES (?, ?, ?)",
            [self.current_position, deck, b""],
        )
        for position, player in enumerate(players):
            cur.execute(
                "INSERT INTO player (game_id, position, hand, palette) VALUES (?, (select seq from sqlite_sequence where name='game'), ?, ?)",
                [position, player[0], player[1]],
            )
        game_id = cur.execute("select seq from sqlite_sequence where name='game'")
        conn.commit()

        self.id = game_id.fetchone()[0]


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


def create_database(schema: str):
    conn = sqlite3.connect(":memory:")
    conn.executescript(schema)
    conn.commit()
    return conn


def copy_database(source_connection, dest_dbname=":memory:"):
    """Return a connection to a new copy of an existing database.
    Raises an sqlite3.OperationalError if the destination already exists.
    """
    script = "".join(source_connection.iterdump())
    dest_conn = sqlite3.connect(dest_dbname)
    dest_conn.executescript(script)
    return dest_conn


if __name__ == "__main__":
    conn = create_database(open("red7.sql").read())
    game = Game(conn, 4)

    print(game.id)
    copy_database(conn, f"logs/{datetime.datetime.now().isoformat()}.db")
