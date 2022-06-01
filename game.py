from deck import Deck
from hand import Hand


class Game:
    MINIMUM_BET = 1

    def __init__(self, player, dealer):
        self.player = player
        self.dealer = dealer
        self.bet = None
        self.deck = Deck()
        
    def start_round(self):
        self.process_bet()
        self.first_dealt_of_cards()
        player_has_blackjack = self.has_naturals("player")
        dealer_has_black_jack = self.has_naturals("dealer")
        if player_has_blackjack:
            self.dealer_unfolds()
            if dealer_has_black_jack:
                print("You tie. Your bet has been returned")
                self.pay_bet(1) #for player 
                self.reset()
            else:
                print(f"Blackjack! You win ${self.bet *1.5}:)")
                self.pay_bet(1.5)
                self.reset()
        else: 
            player_busts = self.players_turn()
            if player_busts:
                print(f"Your hand is over 21 and you loose {self.bet} :(")
                self.reset()
            else:
                
                if dealer_has_black_jack:
                    print("The dealer has black jack you lost!")
                    self.reset()
                else:
                    dealer_busts = self.dealers_turn()
                    if dealer_busts:
                        print(f"The dealer busts, you win ${self.bet}")
                        self.pay_bet(2)
                        self.reset()
                    else:
                        print("The dealer stays.")
                        self.closest_to_twenty_one()
                        self.reset()
                        
    def reset(self):
        self.bet = None
        self.deck = Deck() #fresh deck 
        self.dealer.hand = None #gets rid of current 
        self.player.hand = None #gets rid of current 
        
    def pay_bet(self,amount_multipler):
        self.player.balance += (self.bet + (self.bet * amount_multipler))
        
    def has_naturals(self,user):
        if user == 'player':
            if self.player.hand.get_value() == 21:
                return True
            else:
                return False
        else:
            if self.dealer.hand.get_value() == 21:
                return True
            else:
                return False
             
    def closest_to_twenty_one(self):
        if self.player.hand.get_value() == self.dealer.hand.get_value():
            #tie
            print("You tie. Your bet has been returned")
            self.pay_bet(0)
            
        elif self.player.hand.get_value() > self.dealer.hand.get_value():
            print(f"You win {self.bet}!")
            self.pay_bet(1)
            
        elif self.player.hand.get_value() < self.dealer.hand.get_value():
            print(f"The dealer wins, you loose ${self.bet}")   
    
    def players_turn(self):
        bust = False
        while True:
            answer = input("Would you like to hit or stay? ")
            if answer == "stay":
                break
            elif answer == 'hit':
                new_card = self.deck.deal(1)[0] #the [0] is there because deck.deal() returns list of object, so [0] will 
                #just return one object
                self.player.hit(new_card)
                print("You are dealt:",new_card)
                print("You know have: ", self.player.get_str_hand())
            else:
                print("That is not a valid option.")
            if self.player.hand.get_value() > 21:
                bust = True
                break            
        return bust
            
    def dealers_turn(self):
        self.dealer_unfolds()
        bust = False
        while self.dealer.hand.get_value() <17:
            new_card = self.deck.deal(1)[0]
            self.dealer.hit(new_card)
            print("The dealer hits and is dealt: ",new_card)
            print("The dealer has", self.dealer.get_str_hand())
           
            if self.dealer.hand.get_value() > 21:
                bust = True
                break
        return bust
    
    def dealer_unfolds(self):
        self.dealer.hand.cards[1].face_down = False  #[1] because we want to unhide the second card object in te array
        print("The dealer is has:" ,self.dealer.get_str_hand())
        
    def first_dealt_of_cards(self):
        self.player.hand = Hand(self.deck.deal(2))
        self.dealer.hand = Hand(self.deck.deal(2))
        self.dealer.hand.cards[1].face_down = True
        print("You are dealt with: ",self.player.get_str_hand())
        print("The dealer is dealt with:  ",self.dealer.get_str_hand())

    def process_bet(self):
        while True:
            player_bet = int(input("Place your bet: "))
            if player_bet < self.MINIMUM_BET:
                print(f"The minimum bet is ${self.MINIMUM_BET}.")
                continue
            elif player_bet > self.player.balance:
                print("You do not have sufficient funds.")
                continue
            else:
                self.bet = player_bet
                self.player.balance -= player_bet
                break

    def start_game(self):
        while True:
            if self.player.balance <1:
                print("You ran out of money, Please restart this program to try again. Goodbye")
                break
            player_input = input(f"You are starting with {self.player.balance}. Would you like to play?")
            if player_input != 'yes' :
                break
            self.start_round()
            
        if self.player.balance <=0:
            print("You've ran out of money. Please restart ths program to try again, Goodbye")
            
            
            
            