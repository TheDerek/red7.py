from thederek.red7.cards import Card, Cards, Colour, get_cards


def test_get_cards():
    cards = get_cards("r7b1y3")

    assert cards == Cards(
        [Card(7, Colour.RED), Card(1, Colour.BLUE), Card(3, Colour.YELLOW)]
    )


def test_card_in_cards():
    cards = get_cards("b3o1r7")

    assert Card(1, Colour.ORANGE) in cards
    assert Card(4, Colour.ORANGE) not in cards
