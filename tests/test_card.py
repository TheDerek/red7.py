from thederek.red7 import Cards, Card, Colour


def test_card_in_cards():
    cards = Cards([Card(3, Colour.BLUE), Card(1, Colour.ORANGE), Card(7, Colour.RED)])

    assert Card(1, Colour.ORANGE) in cards
    assert Card(4, Colour.ORANGE) not in cards
