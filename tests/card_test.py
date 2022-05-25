import pytest
from blackjack.card import Card


def test_card_no_values() -> None:
    """Test card with no values should raise a TypeError"""
    with pytest.raises(TypeError):
        test_card = Card()


@pytest.mark.parametrize("suit, face", [('Spade', 'Ace'), ('Heart', 2), ('Diamond', 'Jack'), ('Club', 3)])
def test_card_with_values(suit, face) -> None:
    test_card = Card(suit, face)
    assert test_card.suit == suit
