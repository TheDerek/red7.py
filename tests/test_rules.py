from unittest.mock import Mock
import pytest
import random

from thederek.red7 import rules
from thederek.red7.cards import get_cards, Cards
from thederek.red7.player import Player


def get_player(cards: str):
    return Player(0, Cards([]), get_cards(cards))


@pytest.mark.parametrize(
    "hands, rule",
    [
        (["r7b3r1", "r6b2", "y1", "g5b1"], rules.highest_card),
        (["o3y7", "r6b2", "y1", "g5b1"], rules.highest_card),
        (["o1b1r1r3", "o3r5r7r1b3", "b1v5r2", "g5b1"], rules.most_of_one_number),
        (["v3b1r1r3", "o3r5r7r1b3", "b1v5r2", "g5b1"], rules.most_of_one_number),
    ],
)
def test_rules(hands, rule):
    players = [get_player(hand) for hand in hands]

    # The first player in the list is the winning player, however we want to shuffle the
    # list so that to ensure the rule is not biased towards player position
    winner = players[0]
    random.shuffle(players)

    assert rule(players) == winner
