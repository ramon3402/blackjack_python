from card import Card
class Hand:
    def __init__(self,cards):
        #this will inherit from deck_Deal
        #hand = deck_deal(2)
        self.cards = cards

    def get_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            val = card.value
            if val == 1:
                aces += 1
            else:
                value += min(val, 10)

        if aces == 0:
            return value

        if value + 11 > 21:
            return value + aces
        elif aces == 1:
            return value + 11
        elif value + 11 + (aces - 1) <= 21:
            return value + 11 + (aces - 1)
        else:
            return value + aces
        
    def add(self,card):
        self.cards.append(card)

    def __str__(self):
        string = ""
        for i,card in enumerate(self.cards):
            string += str(card)
            if i != len(self.cards)-1:  
                string += ", "
        return string
            
        
