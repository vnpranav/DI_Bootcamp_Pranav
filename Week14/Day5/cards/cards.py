import random
class Card():
    def __init__(self, value, suit):
        self.__value = value
        self.__suit = suit

    def info(self):
        print(f'{self.__value} of {self.__suit}')
    
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.__cards = []

        # create an unsorted pack of cards
        for suit in suits:
            for value in values:
                newCard = Card(value, suit)
                self.__cards.append(newCard)
    
    def shuffle(self):
        random.shuffle(self.__cards)
        # self.__cards[0].info() : check if cards are shuffled

    def deal(self):
        top = self.__cards.pop(0)
        top.info()
        # print(len(self.__cards)) : check if card has been removed

pack = Deck()
pack.shuffle()
pack.deal()