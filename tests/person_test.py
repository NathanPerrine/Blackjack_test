from blackjack.person import Person, NotACard 
from blackjack.card import Card
import pytest 


@pytest.fixture 
def person() -> Person:
    """Init a new person class for testing"""
    return Person("Nathan")


@pytest.fixture 
def card() -> Card:
    """Card for testing"""
    return Card("Hearts", "Ace")


def test_person_show_empty_hand(capsys, person) -> None:
    """Showing empty hand should print nothing."""
    person.show_hand()
    captured = capsys.readouterr()
    assert captured.out == "You have no cards in hand to show.\n"


def test_person_show_hand_with_cards(capsys, person, card) -> None:
    """Show hand should print card face and suit"""
    person.add_card(card)
    person.show_hand()
    captured = capsys.readouterr()
    assert captured.out == f"{card.face} of {card.suit}\n"


def test_person_add_card(person, card) -> None:
    """Adding a card to a persons hand should add an instance of Card"""
    person.add_card(card)
    assert isinstance(person.hand[0], Card)


def test_person_add_card_not_card(person) -> None:
    """Adding a non card to hand should raise NotACard error"""
    with pytest.raises(NotACard):
        person.add_card(1)


def test_person_get_score_no_hand(capsys, person) -> None:
    person.get_score()
    captured = capsys.readouterr()
    assert captured.out == "You have no cards in hand, no score for you.\n"
