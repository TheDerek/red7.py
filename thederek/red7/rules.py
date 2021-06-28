from thederek.red7.player import Player
from thederek.red7.cards import Cards, Card, Colour


def highest_card(players: list[Player]) -> Player:
    return max(players, key=lambda p: max(p.palette))


RULE_MAPPINGS = {Colour.RED: highest_card}


def get_rule(colour: Colour):
    return RULE_MAPPINGS[colour]
