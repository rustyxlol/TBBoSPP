"""
Project 04
Blackjack

Author: Rusty
GitHub: https://github.com/rustyxlol/TBBoSPP
"""
import random
from collections import namedtuple


SUITE_SYMBOLS = {
    'Spades': chr(9824),
    'Clubs': chr(9827),
    'Hearts': chr(9829),
    'Diamonds': chr(9830),
}
BACKSIDE = 'backside'

Card = namedtuple('Card', ['rank', 'suite'])


class Deck:
    suites = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    ranks = [str(rank) for rank in range(2, 11)] + \
        ['J', 'K', 'Q', 'A']

    def __init__(self):
        self._cards = [Card(rank, suite)
                       for suite in self.suites for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


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


deck = Deck()

display_hands([deck[0]], [deck[0], deck[1]], True)
