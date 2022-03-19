#First Blackjack Project - Udemy Captstone 2


suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 
            'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit,rank))
                
    def shuffle(self):
        # No return needed - does not return instead effects all_cats
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # Note we remove one card from the list of all_cards
        return self.all_cards.pop()    

# class Player is probably not fully needed for this project but imported from seperate project for ease
class Player:
    
    def __init__(self,name):
        self.name = name
         
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
 
#LOGIC GAME EXECUTE
game_continue = True
import random 
game_player = Player('game_player')
dealer = Player('game_dealer')
deck_start = Deck()
game_player_bet = 0
game_player_bank = 100

while game_continue:
    #game set up
    keep_playing = input ('Do you want to keep playing (Yes/No)')
    if keep_playing.capitalize() == "Yes":
        game_continue = True
    elif keep_playing.capitalize() == "No":
        break
    else:
        keep_playing = input ('Do you want to keep playing (Yes/No)')
    
    #instructions and shuffle
    print('\nLets start the hand!')
    print(f'You will start with ${game_player_bank}\n')
    deck_start.shuffle()
        
    #Deal mechanic
    users_cards = []
    users_cards.append(deck_start.deal_one())
    users_cards.append(deck_start.deal_one())
    
    dealer_cards = []
    dealer_cards.append(deck_start.deal_one())
    dealer_cards.append(deck_start.deal_one())
        
    #Bet Mechanic
    bet_loop = True
    
    while bet_loop:
        game_player_bet = int( input ('Please enter your bet: \n'))
        if game_player_bet > game_player_bank:
            print('Not enough available funds\n')

        elif game_player_bet <= game_player_bank:
            print(f'You have made a bet of {game_player_bet}\n')
            bet_loop = False
            break
        else:
            game_player_bet = int( input ('Please enter your bet: '))
        
    #Deal cards
    print ('\nDealing hands now\n')
    print (f'Dealer is showing: ')
    print (dealer_cards[0])
    print ("\n")
    print ('User was dealt: ')
    print (f'{users_cards[0]} and {users_cards[1]}')
    print ("\n")
    
    
    #check value of cards
    user_hand = users_cards[0].value + users_cards[1].value
    dealer_hand = dealer_cards[0].value + dealer_cards[1].value
  
    '''
    this part needs to be cleaned up, figured there's a way to get this chunk down but checking dealer bust inside stand elif 
    seemed to be the easiest way to do this quickly.  Maybe for ease of reading having seperate functions for the checks would be best?
    '''

    hit_check = True
    while hit_check:
        
        hit_q = input('Do you wish to hit or stand?\n')
        if hit_q == 'hit':
            print('Player Hits\n')
            users_cards.append(deck_start.deal_one())
            user_hand = user_hand + users_cards[-1].value
            print(f'You got {users_cards[-1]}, your value is {user_hand}\n')
            if user_hand > 21:
                print ('You busted, your value is {user_hand}\n')
                game_player_bank -= game_player_bet
                break 
        #check bust
        elif user_hand > 21:
            print ('You busted, your value is {user_hand}\n')
            game_player_bank -= game_player_bet
            break 
        
        elif hit_q == 'stand':
            #check dealer bust
            if dealer_hand < 16:
                dealer_cards.append(deck_start.deal_one())
                dealer_hand = dealer_hand + dealer_cards[-1].value
                print(f'Dealer flipped {dealer_cards[1]} and drew {dealer_cards[-1]}, their value is {dealer_hand}\n')
                if dealer_hand > 21:
                    print('Dealer Busted!\n')
                    game_player_bank += game_player_bet
                    break
                elif dealer_hand < user_hand:
                    print('You won the hand!\n')
                    game_player_bank += game_player_bet
                    break
                elif dealer_hand >= user_hand:
                    print('You lost the hand!\n')
                    game_player_bank -= game_player_bet
                    break
                elif dealer_hand > 21:
                    print('Dealer Busted!\n')
                    game_player_bank += game_player_bet
                    break
            elif dealer_hand < user_hand:
                print(f'You won the hand! Dealer had {dealer_cards[1]}, their value is {dealer_hand}\n')
                game_player_bank += game_player_bet
                break
            elif dealer_hand >= user_hand:
                print(f'You lost the hand! Dealer had {dealer_cards[1]}, their value is {dealer_hand}\n')
                game_player_bank -= game_player_bet
                break
        #fund check        
        elif game_player_bank <= 0:
            print ('you are out of funds')
            break
        else: 
            hit_q = input('Do you wish to hit or stand?')
    

    