import pytest
from blackjack.blackjack import Card



def test_card_no_values() -> None:
    """Test card with no values should raise a TypeError"""
    with pytest.raises(TypeError):
        test_card = Card()

def test_card_with_values() -> None:
    test_card = Card('Heart', 'Ace')
    assert test_card.suit == 'Heart'
    assert test_card.face == 'Ace'