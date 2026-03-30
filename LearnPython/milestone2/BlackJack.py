import random

suits = ['Hearts','Spades','Diamonds','Clubs']
ranks = ['two','three','four','five','six','seven','eight',
         'nine','ten','jack','queen','king','ace']
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
          'nine':9,'ten':10,'jack':10,'queen':10,'king':10,'ace':10}

playing = True

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f'{self.rank.capitalize()} of {self.suit}'

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        ds= f'Deck has {len(self.deck)} cards'
        for card in self.deck:
            ds=ds+','+card.__str__()
        return ds

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank.lower() == 'ace':
            self.aces+=1

    # If hand value is > 21 then adjust ace value from 11 to 1
    def adjust_for_ace(self):
        if self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

class Chips:

    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

## Functions
def take_bet(chips):
    while True:
        try:
            chips.bet = int(input('How many chips would you like to bet?'))
        except ValueError:
            print('Sorry! Bet must be an integer.')
        else:
            if chips.bet > chips.total:
                print(f'Sorry! You have only {chips.total}')
            else:
                break

def hit(deck,hand):

    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# This function should accept the deck and the player's hand as arguments, and assign playing as a global variable.
# If the Player Hits, employ the hit() function above. If the Player Stands,
# set the playing variable to False - this will control the behavior of a while loop later on in our code.
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop

    while True:
        hs = input('Would you like to hit or stand (h/s)?')
        if hs.lower() == 'h':
            hit(deck,hand)
            break
        elif hs.lower() == 's':
            print("Player stands dealer's turn.")
            playing = False
            break
        else:
            print('Please enter a valid input.')

# When the game starts, and after each time Player takes a card,
# the dealer's first card is hidden and all of Player's cards are visible.
# At the end of the hand all cards are shown, and you may want to show each hand's total value.
# Write a function for each of these scenarios.
def show_some(player,dealer):

    # Show only one of the dealers cards
    #dealer.cards will be a list of 2 cards
    print("Dealer's Hand : ")
    print("FIRST card hidden.")
    print(dealer.cards[1])
    #Show both of the player cards
    print("Player's Hand : ")
    for card in player.cards:
        print(card)

def show_all(player,dealer):
    # Show all of the dealers cards
    print("Dealer's Hand : ")
    for card in dealer.cards:
        print(card)
    # Calculate and display value of dealer's hand
    print(f"Value of Dealer's hand is {dealer.value}")
    #Show both of the player cards
    print("Player's Hand : ")
    for card in player.cards:
        print(card)
        # Calculate and display value of player's hand
    print(f"Value of Player's hand is {player.value}")

# Write functions to handle end of game scenarios
# Remember to pass player's hand, dealer's hand and chips as needed.
def player_busts(player,dealer,chips):
    print('PLAYER BUSTS!')
    chips.lose_bet()


def player_wins(player,dealer,chips):
    print('PLAYER WINS!')
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print('PLAYER WINS! DEALER BUSTS.')
    chips.win_bet()

def dealer_wins(player,dealer,chips):
    print('DEALER WINS!')
    chips.lose_bet()

#Tie between Dealer and Player
def push(player,dealer):
    print("Dealer and Player tie! PUSH")

if __name__ == '__main__':
    while True:
        # Print an opening statement
        print('Welcome to Black Jack!!!')

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()


        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())
        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
        # Set up the Player's chips
        player_chips = Chips()

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)


        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck,player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand,dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand,dealer_hand,player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        if player_hand.value <= 21:
            while dealer_hand.value < 17:
                hit(deck,dealer_hand)

            # Show all cards
            show_all(player_hand,dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand,dealer_hand,player_chips)
            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand,dealer_hand,player_chips)
            else:
                push(player_hand,dealer_hand)

        # Inform Player of their chips total
        print(f'\n Player total chips are at {player_chips.total}')
        # Ask to play again
        new_game = input("Would you loke to play another hand? (y/n)")
        if new_game.lower() == 'y':
            playing = True
        else:
            print('Thank you for playing!')
            break
