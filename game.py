import random


class Game:

    def __init__(self):
        self.cards = self.initialize_deck()

    @staticmethod
    def initialize_deck():
        start_deck = [0, 0, 0]
        for number in range(1, 11):
            if number != 10:
                start_deck += [number] * 5
            elif number == 10:
                start_deck += [number] * 8
        return start_deck


print("bbb")

# Example usage:
game = Game()

print(game.cards)
