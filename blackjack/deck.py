from blackjack.card import Card
from random import shuffle

class Deck:
    def __init__(self):
        self.decklist = []

    def generate_deck(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        faces = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King', 'Ace']
        self.decklist = [Card(suit, face) for suit in suits for face in faces]
        

    def shuffle_deck(self):
        shuffle(self.decklist)