import random

class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        if self.value == 14:
            value = "A"
        elif self.value == 13:
            value = "K"
        elif self.value == 12:
            value = "Q"
        elif self.value == 11:
            value = "J"
        else:
            value = self.value
        if self.suit == 'H':
            suit = "♥"
        elif self.suit == 'C':
            suit = "♣"
        elif self.suit == 'D':
            suit = "♦"
        elif self.suit == 'S':
            suit = "♠"
        return "{}{}".format(value, suit)

    def show(self):
        if self.value == 14:
            value = "A"
        elif self.value == 13:
            value = "K"
        elif self.value == 12:
            value = "Q"
        elif self.value == 11:
            value = "J"
        else:
            value = self.value
        if self.suit == 'H':
            suit = "♥"
        elif self.suit == 'C':
            suit = "♣"
        elif self.suit == 'D':
            suit = "♦"
        elif self.suit == 'S':
            suit = "♠"
        return "{}{}".format(value, suit)


class Deck():
    def __init__(self):
        self.cards = []
        self.create()

    def show(self):
        for card in self.cards:
            print(card)

    def create(self):
        # Function to build a deck of cards
        self.cards = []
        for value in range(14,1,-1):
            for suit in ['H', 'C', 'D', 'S']:
                self.cards.append(Card(value, suit))
        return True

    def shuffle(self):
        # Function to shuffle the deck
        random.shuffle(self.cards)
        return True

    def draw(self):
        randomFromDeck = random.choice(self.cards)
        self.cards.remove(randomFromDeck)
        return randomFromDeck


class Player():
    def __init__(self, name):
        self.name = name
        self.hand1 = []
        self.hand2 = []
        self.handRank = 0

    def show(self):
        for card in self.hand:
            print(card)


class Board():
    def __init__(self):
        self.flop1 = []
        self.flop2 = []
        self.flop3 = []
        self.turn = []
        self.river = []
