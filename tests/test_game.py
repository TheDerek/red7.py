from thederek.red7.game import Game
from thederek.red7.player import Player
from thederek.red7.cards import get_cards, Cards


def test_is_current_player_winning():
    game_args = {
        "deck": Cards(),
        "canvas": get_cards("r1"),
        "players": [
            # The losing player with highest card Yellow3
            Player(0, Cards(), get_cards("v1y3")),
            # The winning player with highest card Orange3
            Player(1, Cards(), get_cards("b2o3")),
        ],
    }

    winning = Game(**game_args, current_player_idx=1)
    losing = Game(**game_args, current_player_idx=0)

    assert winning.is_current_player_winning()
    assert not losing.is_current_player_winning()
