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
    cards_on_table =[]
    round_num = 1
    deal_one_from_each_player()
    while len(vinu.all_cards) != 0 and len(ramya.all_cards)!= 0:

        logging.debug(f'Vinu - {vinu_current_card.suit} - {vinu_current_card.value}')
        logging.debug(f'Ramya - {ramya_current_card.suit} - {ramya_current_card.value}')
        logging.debug(f'Cards - {cards_on_table}')
        if vinu_current_card.value < ramya_current_card.value:
            ramya.add_cards(cards_on_table)
            logging.debug(f'{len(cards_on_table)} Cards moved to Ramya')
            cards_on_table.clear()
            deal_one_from_each_player()
        elif vinu_current_card.value > ramya_current_card.value:
            vinu.add_cards(cards_on_table)
            logging.debug(f'{len(cards_on_table)} Cards moved to Vinu')
            cards_on_table.clear()
            deal_one_from_each_player()
        else: # war deal 3
            logging.info('WAR!!!')
            for num in range(3):
                deal_one_from_each_player()

        logging.info(f'After round {round_num} {vinu} and {ramya} - Cards on table - {len(cards_on_table)}')
        round_num+=1

    if len(cards_on_table) > 0:
        if len(vinu.all_cards) == 0:
            ramya.add_cards(cards_on_table)
            logging.info('Ramya WINS!!!')
        else:
            vinu.add_cards(cards_on_table)
            logging.info('Vinu WINS!!!')

logging.info(f'Final Score - Vinu - {len(vinu.all_cards)} and Ramya - {len(ramya.all_cards)}')


