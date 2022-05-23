"""
Project 04
Blackjack

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
import random
from collections import namedtuple
import sys

SUITE_SYMBOLS = {
    'Spades': chr(9824),
    'Clubs': chr(9827),
    'Hearts': chr(9829),
    'Diamonds': chr(9830),
}
BACKSIDE = 'backside'

Card = namedtuple('Card', ['rank', 'suite'])


class Deck:
    "Generates all 52 cards"
    suites = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    ranks = [str(rank) for rank in range(2, 11)] + \
        ['J', 'K', 'Q', 'A']

    def __init__(self):
        self._cards = [Card(rank, suite)
                       for suite in self.suites for rank in self.ranks]
        random.shuffle(self._cards)

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def pop(self):
        return self._cards.pop()


def display_hands(player_hand, dealer_hand, show_dealer_all=False):
    "Displays cards of player and dealer"
    print("Dealer's Hand: ")
    if show_dealer_all:
        display_card(dealer_hand)
    else:
        display_card([BACKSIDE] + dealer_hand[1:])
    print("Player's Hand:")
    display_card(player_hand)


def display_card(cards):
    "Displays cards containing Card in ASCII art"
    rows = ['', '', '']
    for card in cards:
        if card == BACKSIDE:
            rows[0] += "|##".ljust(4) + '| '
            rows[1] += '| # | '
            rows[2] += '|' + '##'.rjust(3) + '| '
        else:
            rank, suite = card
            rows[0] += f"|{rank}".ljust(4) + '| '
            rows[1] += f'| {SUITE_SYMBOLS[suite]} | '
            rows[2] += '|' + f'{rank}'.rjust(3) + '| '

    for row in rows:
        print(row)


def display_rules():
    "Displays rules"
    print("*"*30)
    print("Rules".rjust(17))
    print("*"*30)
    print("Try to get as close to 21 without going over.")
    print("Kings, Queens, and Jacks are worth 10 points.")
    print("Aces are worth 1 or 11 points.")
    print("Cards 2 through 10 are worth their face value.")
    print("(H)it to take another card.")
    print("(S)tand to stop taking cards.")
    print("On your first play, you can (D)ouble down to increase your bet")
    print("but must hit exactly one more time before standing.")
    print("In case of a tie, the bet is returned to the player.")
    print("The dealer stops hitting at 17.")


def get_bet(total_money):
    print("Money: ", total_money)
    while True:
        print("Press q to quit")
        bet = input(f"Enter bet amount(1 - {total_money}): ")
        if bet == 'q':
            sys.exit()
        if not bet.isdecimal() or int(bet) >= total_money:
            continue

        return int(bet)


def get_hand_value(cards):
    value = 0
    num_aces = 0
    for card in cards:
        if card.rank in ('K', 'Q', 'J'):
            value += 10
        elif card.rank == 'A':  # evaluate aces last
            num_aces += 1
        else:
            value += int(card.rank)

    value += num_aces
    for _ in range(num_aces):
        if value + 10 < 21:
            value += 10

    return value


def get_move():
    while True:
        print("(H)it, (S)tand, (Q)uit")
        move = input("> ").lower()
        if move in ('h', 's'):
            return move
        if move.startswith('q'):
            print("Wow you really did that")
            sys.exit(0)


def main():
    print("WELCOME TO BLACKJACK")
    display_rules()
    money = 5000
    while True:
        if money <= 0:
            print("You cannot enter da casino")
            break

        bet = get_bet(money)

        deck = Deck()

        player_hand = [deck.pop(), deck.pop()]
        dealer_hand = [deck.pop(), deck.pop()]

        while True:
            # Play until bust or stand
            display_hands(player_hand, dealer_hand, False)

            if get_hand_value(player_hand) > 21:
                break

            move = get_move()

            if move == 'h':
                new_card = deck.pop()
                player_hand.append(new_card)

            if get_hand_value(player_hand) > 21:
                break

            if move == 's':
                break

        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) <= 17:
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                    break

        display_hands(player_hand, dealer_hand, True)

        player_hand_value = get_hand_value(player_hand)
        dealer_hand_value = get_hand_value(dealer_hand)

        if dealer_hand_value >= 21:
            money += bet
            print("The dealer BUSTS! You win!")
        elif player_hand_value >= 21:
            money -= bet
            print("You BUST!")
        elif player_hand_value <= dealer_hand_value:
            money -= bet
            print("You lose!")
        elif player_hand_value == dealer_hand_value:
            print("Tie! You get the money back!")
        else:
            print(f"You win ${bet}")
            money += bet

        print("Press ENTER to play again\n")


main()
