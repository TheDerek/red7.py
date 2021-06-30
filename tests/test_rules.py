from unittest.mock import Mock
import pytest

from thederek.red7 import rules
from thederek.red7.cards import get_cards
from thederek.red7.player import Player


def get_player(cards: str):
    player = Mock(spec=Player)
    player.palette = get_cards(cards)
    return player


@pytest.mark.parametrize(
    "palette_winner,palette_loser,rule",
    [
        ("r7b3r1", rules.highest_card),
        (
            ["red1", "red2", "violet4"],
            ["blue1", "blue2", "blue3"],
            rules.most_of_one_number,
        ),
        (
            ["blue2", "red2", "violet4"],
            ["blue1", "red1", "blue3"],
            rules.most_of_one_number,
        ),
    ],
)
def test_rules(palette_winner, palette_loser, rule):
    palette_winner = [cards[card_name] for card_name in palette_winner]
    palette_loser = [cards[card_name] for card_name in palette_loser]

    assert rule(palette_winner, palette_loser) == palette_winner
    assert rule(palette_loser, palette_winner) == palette_winner


@pytest.mark.parametrize(
    "palette,freq,highest_card",
    [
        (["blue1", "blue2", "yellow1", "yellow2", "yellow3"], 2, "yellow2"),
        (["blue1", "red1", "yellow1", "blue2", "violet2"], 3, "red1"),
        (["orange2", "yellow2", "red2"], 3, "red2"),
        (["orange4", "yellow3", "red2"], 1, "orange4"),
    ],
)
def test_most_of_one_number_in_palette(palette, freq, highest_card):
    palette = [cards[card_name] for card_name in palette]
    highest_card = cards[highest_card]

    assert rules._most_of_one_number_in_palette(palette) == (freq, highest_card)
