import random


class Game:

    def __init__(self):
        self.cards = self.initialize_deck()
        self.lucky_card = self.get_card()
        self.cards_thrown = []

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

    def get_card(self, take_from_stack=True):
        if take_from_stack == False:
            last_thrown = self.cards_thrown[-1]
            return last_thrown
        else:
            card = self.cards[-1]
            self.cards[:] = self.cards[:-1]
            return card

    def throw_card(self, card):
        self.cards_thrown.append(card)


# Example usage:
game = Game()

# print(game.cards)
# print(game.get_card())
# print(game.cards)
