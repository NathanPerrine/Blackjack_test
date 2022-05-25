class InvalidValueError(Exception):
    pass


class Card():
    def __init__(self, suit, face):
        if suit not in {'Hearts', 'Diamonds', 'Spades', 'Clubs'}:
            raise InvalidValueError("Suits can only be Hearts, Diamonds, Spades, Clubs")
        if face not in {2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace'}:
            raise InvalidValueError("Face can only be 2,3,4,5,6,7,8,9,10, 'Jack', 'Queen', 'King', 'Ace'")

        self.suit = suit
        self.face = face