import pytest

from thederek.red7 import Player, Cards, Card, Colour, GameLogicError


def test_play():
    player = Player(
        0,
        hand=Cards([Card(7, Colour.RED), Card(4, Colour.BLUE)]),
        palette=Cards([Card(3, Colour.GREEN)]),
    )
    new_player = player.play(Card(4, Colour.BLUE))

    assert new_player.hand == Cards([Card(7, Colour.RED)])
    assert new_player.palette == Cards([Card(3, Colour.GREEN), Card(4, Colour.BLUE)])

def test_play_invalid_card():
    player = Player(
        0,
        hand=Cards([Card(7, Colour.RED), Card(4, Colour.BLUE)]),
        palette=Cards([Card(3, Colour.GREEN)]),
    )

    with pytest.raises(GameLogicError):
        player.play(Card(1, Colour.BLUE))
