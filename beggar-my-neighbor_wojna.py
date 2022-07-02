import os
import random


def clean_console():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


class Card:
    powers = {'Ace':14, 'King': 13, 'Queen': 12, 'Jack': 11}
    suits = ('Clubs', 'Diamonds', 'Hearts', 'Spades')
    def __init__(self, symbol :str, suit :str):
        self.symbol = symbol
        if self.symbol.isdigit() and int(self.symbol) in [i for i in range(2, 11)]:
            self.power = int(self.symbol)
        elif self.symbol in Card.powers.keys():
            self.power = Card.powers[self.symbol]
        else:
            raise "Bad symbol mordo"
        if suit in Card.suits:
            self.suit = suit
        else:
            raise "Bad suit mordo"

    def __repr__(self):
        return f'{self.symbol} {self.suit}'


class Deck:
    def __init__(self):
        self.cards = []
        for suit in Card.suits:
            for symbol in list(Card.powers.keys()) + [str(i) for i in range(2, 11)]:
                self.cards.append(Card(symbol, suit))


class Player:
    def __init__(self, name :str):
        self.name = name
        self.deck = []
        self.score = len(self.deck)

    def __repr__(self):
        return f'Player {self.name}\nScore{self.score}'

    def current_card(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck[-1]

class Game:
    def __init__(self, player1 :Player, player2 :Player):
        self.player1 = player1
        self.player2 = player2
        self.deck = Deck()
        self.deposit = []
        self.round = 0
        self.prepare_game()

    def prepare_game(self):
        random.shuffle(self.deck.cards)
        while len(self.deck.cards) != 0:
            self.player1.deck.append(self.deck.cards.pop())
            self.player2.deck.append(self.deck.cards.pop())

    def fight(self):
        # clean_console()
        self.round += 1
        if self.player1.current_card() and self.player2.current_card():
            temp = ''
            temp += '\n' + f'Round {self.round}'.center(40) + '\n\n'
            temp += self.player1.name.center(20)
            temp += self.player2.name.center(20) + '\n'
            temp += self.player1.current_card().__repr__().center(20)
            temp += self.player2.current_card().__repr__().center(20) + '\n'
            temp += str(len(self.player1.deck)).center(20)
            temp += str(len(self.player2.deck)).center(20) + '\n'
            if self.player1.current_card().power > self.player2.current_card().power:
                temp += f'\nPlayer {self.player1.name} has the highest card'
                self.player1.deck.insert(0, self.player2.deck.pop())
                self.player1.deck.insert(0, self.player1.deck.pop())
                self.get_deposit(self.player1)
                print(temp)
                input('Enter to continue... ')
                clean_console()
            elif self.player2.current_card().power > self.player1.current_card().power:
                temp += f'\nPlayer {self.player2.name} has the highest card'
                self.player2.deck.insert(0, self.player1.deck.pop())
                self.player2.deck.insert(0, self.player2.deck.pop())
                self.get_deposit(self.player2)
                print(temp)
                input('Enter to continue... ')
                clean_console()
            else:
                print(temp)
                self.war()
        else:
            self.end()

    def war(self):
        if len(self.player1.deck) >= 2 and len(self.player2.deck) >= 2:
            print('War')
            self.deposit.append(self.player1.deck.pop())
            self.deposit.append(self.player2.deck.pop())
        else:
            self.end()

    def get_deposit(self, player :Player):
        while len(self.deposit) != 0:
            player.deck.insert(0, self.deposit.pop())

    def end(self):
        print('\n\n')
        if len(self.player1.deck) > len(self.player1.deck):
            print(f'Player {self.player1.name} won')
        else:
            print(f'Player {self.player2.name} won')
        input('Enter to close... ')
        exit()
        raise StopIteration

def main():
    game = Game(Player('Dario'), Player('Andrzej'))
    while True:
        game.fight()


if __name__ == '__main__':
    main()