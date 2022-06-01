import random
from card import Card
class Deck:
    def __init__(self):
        self.deck_cards = [] #check
        self.create_deck()
        self.shuffle()

    def create_deck(self):
        for suit in range(4):
            for card in range(1,14):
                new_card = Card(suit, card) 
                self.deck_cards.append(new_card) #list of objects cards
                
                
                
    def shuffle(self):
        random.shuffle(self.deck_cards)

    def deal(self, num_cards):
        dealt_cards = []
        for i in range(num_cards):
            dealt_cards.append(self.deck_cards.pop())
            
        return dealt_cards
