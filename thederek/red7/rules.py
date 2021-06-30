from collections import Counter

from thederek.red7.player import Player
from thederek.red7.cards import Cards, Card, Colour


def highest_card(players: list[Player]) -> Player:
    return max(players, key=lambda p: max(p.palette))


def most_of_one_number(players: list[Player]):
    def most(player: Player) -> tuple(int, Card):
        # Find the most common number in the players palette
        most_common_number: int = Counter(
            [card.number for card in player.palette]
        ).most_common(1)[0][0]

        # Find the highest card that has that number
        highest_card = max(
            [card for card in player.palette if card.number == most_common_number]
        )

        return most_common_number, highest_card

    values = {player: most(player) for player in players}
    return max(players, key=lambda p: values[p])


RULE_MAPPINGS = {Colour.RED: highest_card, Colour.ORANGE: most_of_one_number}


def get_rule(colour: Colour):
    return RULE_MAPPINGS[colour]
