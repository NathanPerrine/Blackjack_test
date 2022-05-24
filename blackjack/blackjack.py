from blackjack.deck import Deck





def main():
    deck = Deck()
    deck.generate_deck()
    deck.shuffle_deck()

if __name__ == "__main__":
    main()