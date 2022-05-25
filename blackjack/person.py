from blackjack.card import Card


class NotACard(Exception):
    pass

class Person():
    def __init__(self, name):
        self.name = name
        self.hand = []

    def show_hand(self):
        if self.hand == []:
            print("You have no cards in hand to show.")
        else:
            for card in self.hand:
                print(f"{card.face} of {card.suit}")

    def add_card(self, card):
        if not isinstance(card, Card):
            raise NotACard("You can only add a Card object to a persons hand.")
        self.hand.append(card)

    def get_score(self):
        if self.hand == []:
            print("You have no cards in hand, no score for you.")
        score = 0 
        face_cards = {"Jack", "Queen", "King"}
        for card in self.hand:
            if card.face.isnumeric():
                score += card.face
            elif card.face in face_cards:
                score += 10 
            elif card.face == "Ace":
                if score + 11 > 21:
                    score += 1
                else:
                    score += 11