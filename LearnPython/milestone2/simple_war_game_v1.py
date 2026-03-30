import random,logging,sys

# Set the root logger level to DEBUG
# Logging stream directed to sysout because print() and logging use two different output streams
# that are handled differently by your terminal or IDE. So order of printing may not be sequential.
logging.basicConfig(level=logging.INFO,
                    stream=sys.stdout,
                    format='%(levelname)s: %(message)s'
                    )

suits = ['Hearts','Spades','Diamonds','Clubs']
ranks = ['two','three','four','five','six','seven','eight',
         'nine','ten','jack','queen','king','ace']
values = {'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
          'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':14}
CARDS_TO_DEAL_WHEN_AT_WAR = 5
class Card:

    def __init__(self,rank,suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank.lower()]

    def __str__(self):
        return self.rank.capitalize() + ' of ' + self.suit

class Deck:
    '''
    A Deck will be made up of multiple Cards. Which mean's we will actually use
    the Card class within the __init__ of the Deck class.
    '''
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(rank,suit))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()

    def __str__(self):
        return f'Deck has {len(self.all_cards)}'

class Player:
    def __init__(self,name):
        self.name = name
        self.all_cards = []

    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def remove_one(self):
        return self.all_cards.pop(0)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards'


def deal_one_from_each_player():
    global vinu_current_card, ramya_current_card

    if len(vinu.all_cards) !=0 and len(ramya.all_cards) != 0:
        vinu_current_card = vinu.remove_one()
        ramya_current_card = ramya.remove_one()
        cards_on_table.append(vinu_current_card)
        cards_on_table.append(ramya_current_card)


if __name__ == '__main__':
    new_deck = Deck()
    new_deck.shuffle()

    logging.info(new_deck)
    # cards = [new_deck.deal_one(),new_deck.deal_one(),new_deck.deal_one(),new_deck.deal_one(),new_deck.deal_one()]
    # for card in cards:
    #     print(card)
    vinu = Player('Vinu')
    ramya = Player('Ramya')
    logging.info("Dealing cards to both players")
    while len(new_deck.all_cards) > 1 :
       vinu.add_cards(new_deck.deal_one())
       ramya.add_cards(new_deck.deal_one())

    logging.info(vinu)
    logging.info(ramya)

    logging.info('Lets start War Game')

    game_on = True
    round_num = 0

    while game_on:
        round_num+=1
        logging.info(f'At round {round_num} - {vinu} and {ramya}')
        if len(vinu.all_cards) == 0:
            logging.info("Vinu's cards are exhausted. Ramya WINS!!!")
            game_on = False
            break
        elif len(ramya.all_cards) == 0:
            logging.info("Ramya's cards are exhausted. Vinu WINS!!!")
            game_on = False
            break

        cards_on_table = []
        vinu_current_card = vinu.remove_one()
        ramya_current_card = ramya.remove_one()
        cards_on_table.append(vinu_current_card)
        cards_on_table.append(ramya_current_card)

        at_war = True

        while at_war:

            if vinu_current_card.value > ramya_current_card.value:
                vinu.add_cards(cards_on_table)
                at_war = False
            elif ramya_current_card.value > vinu_current_card.value:
                ramya.add_cards(cards_on_table)
                at_war = False
            else: # At war. Deal 3 cards
                logging.info("At WAR!!!")
                if len(vinu.all_cards) < CARDS_TO_DEAL_WHEN_AT_WAR:
                    logging.info('Vinu unable to declare war. Ramya WINS!!!')
                    game_on = False
                    break
                elif len(ramya.all_cards) < CARDS_TO_DEAL_WHEN_AT_WAR:
                    logging.info('Ramya unable to declare war. Vinu WINS!!!')
                    game_on = False
                    break
                else:
                    for num in range(CARDS_TO_DEAL_WHEN_AT_WAR):
                        vinu_current_card = vinu.remove_one()
                        ramya_current_card = ramya.remove_one()
                        cards_on_table.append(vinu_current_card)
                        cards_on_table.append(ramya_current_card)



logging.info(f'Final Score - Vinu - {len(vinu.all_cards)} and Ramya - {len(ramya.all_cards)}')


