import pytest
from blackjack.card import Card, InvalidValueError


def test_card_no_values() -> None:
    """Test card with no values should raise a TypeError"""
    with pytest.raises(TypeError):
        test_card = Card()


def test_card_with_invalid_suit() -> None:
    with pytest.raises(InvalidValueError):
        test_card = Card("Hello World", 2)


def test_card_with_invalid_face() -> None:
    with pytest.raises(InvalidValueError):
        test_card = Card("Hearts", 12)


@pytest.mark.parametrize("suit, face", [('Spades', 'Ace'), ('Hearts', 2), ('Diamonds', 'Jack'), ('Clubs', 3)])
def test_card_with_values(suit, face) -> None:
    test_card = Card(suit, face)
    assert test_card.suit == suit