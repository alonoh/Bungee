import random


class Game:

    def __init__(self):
        self.cards = self.initialize_deck()
        self.lucky_card = self.get_card()

    @staticmethod
    def initialize_deck():
        start_deck = [0, 0, 0]
        for number in range(1, 11):
            if number != 10:
                start_deck += [number] * 5
            elif number == 10:
                start_deck += [number] * 8
        random.shuffle(start_deck)
        return start_deck

    def get_card(self):
        card = self.cards[-1]
        self.cards[:] = self.cards[0:-1]
        return card

    def thrown_card(self, card):
        cards_thrown = []
        new_cards_thrown = cards_thrown + card

# Example usage:
game = Game()

# print(game.cards)
# print(game.get_card())
# print(game.cards)
