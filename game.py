import random
from string import Template

class Card(object):
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = self.card_value()

    def card_value(self):
        """ Количество очков, которое дает карта """
        if self.rank in "T":
            return 10
        elif self.rank in "J":
            return 11
        elif self.rank in "Q":
            return 12
        elif self.rank in "K":
            return 13
        elif self.rank in "A":
            return 14
        else:
            return " 123456789".index(self.rank) #Число очков за любую карту

    def get_rank(self):
        return self.rank

    def __str__(self):
        return "%s%s" % (self.rank, self.suit)

class Deck(object):
    def __init__(self):
        ranks = "6789TJQKA" #ранги
        suits = "DCHS" #масти
        self.cards = [Card(r,s) for r in ranks for s in suits] #генератор колоды из 36 карт
        random.shuffle(self.cards) #перетасовка колоды
        print('\nNumber of cards: ' + str(len(self.cards)))

    def deal_card(self):
        """ Сдача карты """
        return self.cards.pop()

    def trump_card(self):
        """ Определение козырной карты """
        trmp_card = self.cards.pop()
        self.get_trump_deck(trmp_card.suit)
        #return print(self.cards.pop().suit)
        #return self.cards.pop()
        return trmp_card

    def get_trump_deck(self, trump_suit):
        """ Добавление очков для козырной карты """
        for card in self.cards:
            if  trump_suit == card.suit:
                card.value += 10
        
class Hand(object):
    def __init__(self, name):
        self.name = name #имя игрока
        self.cards = [] #пустая рука

    def add_card(self, card):
        """ Добавление карты в руки """
        self.cards.append(card)

    def get_value(self):
        """ Метоод получения числа очков на руке """
        result = 0
        for card in self.cards:
            result +=  card.value 
        return result

    def __str__(self):
        text = "%s contains: \n" % self.name
        for card in self.cards:
            text += str(card) + " "
        text += "\nHand value: " + str(self.get_value()) + "\n"
        return text

def new_game():
    """ Создание новой игры """
    players = int(input('\nEnter the number of players: '))
    main(players)

def create_hands(players):
    """ Создание игроков с картами на руках """
    d = Deck() # создание колоды
    players_hands_values = [] 
    print('\nTrump card: ' + str(d.trump_card())+'\n')
    for i in range(1,players + 1): # цикл для создания рук игроков
        player = Template('Player $i').substitute(i=i) # динамическое создание имени игрока
        player_hand = Hand(player)
        for j in range(0,6): # добавление карт в руки игрока
             player_hand.add_card(d.deal_card())
        players_hands_values.append(player_hand.get_value()) # добавление значения текущего игрока в список
        print(player_hand)
    return players_hands_values  # возвращает список значений   

def main(players):
    """ Алгоритм работы игры """
    if players == 1:
        print('\nMin number of players is 2!!!')
        return new_game()
    elif players >= 6:
        print('\nMax number of players is 5!!!')
        return new_game()
    players_hands_values = create_hands(players) 
    maxVal = max(players_hands_values) 
    print('Max value: '+str(maxVal))
    numWinner = players_hands_values.index(maxVal) + 1 # вычисление номера игрока - победителя по индексу в списке
    print(Template('Player $numWinner wins !!!').substitute(
            numWinner=numWinner
        ))

new_game()