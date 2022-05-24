from dataclasses import dataclass
from collections import Counter
from random import shuffle 

class Deck():
    def __init__(self):
        self.decklist = []

    def generate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.decklist = [Card(suit, face) for suit in suits for face in faces]
        

    def shuffle_deck(self):
        shuffle(self.decklist)

@dataclass
class Card():
    suit: str
    face: str

def main():
    deck = Deck()
    deck.generate_deck()
    deck.shuffle_deck()

if __name__ == "__main__":
    main()