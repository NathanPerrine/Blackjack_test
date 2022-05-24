import pytest
from collections import Counter
from blackjack.blackjack import Deck

@pytest.fixture
def empty_deck() -> Deck():
    """Returns an empty deck"""
    return Deck()

@pytest.fixture 
def deck_with_cards() -> Deck():
    """Returns a deck with cards generated"""
    deck = Deck()
    deck.generate_deck()
    return deck

def test_deck_generate_deck(empty_deck) -> None:
    """generate_deck should generate a decklist of 52 cards"""
    empty_deck.generate_deck()
    assert len(empty_deck.decklist) == 52

def test_deck_card_count(deck_with_cards) -> None:
    """deck with generated deck should have four of each card face, 13 faces, == 52 cards"""
    card_faces = Counter([card.face for card in deck_with_cards.decklist])
    assert card_faces.total() == 52

def test_deck_shuffle_deck(deck_with_cards) -> None:
    non_shuffle = deck_with_cards.decklist[:]
    deck_with_cards.shuffle_deck()
    assert non_shuffle != deck_with_cards.decklist