import random

class CardDeck:
    suits = ['diamonds', 'hearts', 'spades', 'clubs']
    special_cards = {'ace': 1,
                     'jack': 10,
                     'queen': 10,
                     'king': 10}

    def __init__(self):
        self.generate_deck()

    def generate_deck(self):
        picture_cards = ['jack', 'queen', 'king']
        values = []

        for i in range(1, 11):
            if i == 1:
                card = 'ace'
                values.append(card)

            elif i == 10:
                values.append(str(i))
                for card in picture_cards:
                    values.append(card)

            else:
                values.append(str(i))

        deck = []
        for suit in self.suits:
            for val in values:
                card = val + '-' + suit
                deck.append(card)

        # Shuffling Deck
        random.shuffle(deck)

        self.deck = deck

    def deal_cards(self, number_of_cards):
        hand = []
        for i in range(number_of_cards):
            hand.append(self.deck[i])

        print('\n')
        print("This is you hand, hope it's a good one!")
        for card in hand:
            card = card.replace('-', ' of ')
            print(card)

        sum = self.sum_cards(hand)
        print('\n')
        print('The sum of your card values is ' + str(sum))

    def sum_cards(self, hand):
        sum = 0
        for card in hand:
            card = card.split('-')[0]
            if card in self.special_cards.keys():
                value = self.special_cards[card]
                sum += value
            else:
                sum += int(card)

        return sum

# Generating Deck:
deck = CardDeck()

# Input how many cards you'd like
deck.deal_cards(5)

