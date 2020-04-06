#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import argparse
import sys
import signal

from tictactoe import TicTacToe
from agents import RandomTicTacToeAgent


parser = argparse.ArgumentParser(description='Train a tic tac toe agent')
parser.add_argument('--verbose', action='store_const',
                    const=True, default=False,
                    help='Print result of the game')
parser.add_argument('-n', type=int, default=1, help='Number of games to play')
args = parser.parse_args()

for i in range(args.n):

    tictactoe = TicTacToe()

    Player1 = RandomTicTacToeAgent(tictactoe)
    Player2 = RandomTicTacToeAgent(tictactoe)

    tictactoe.add_agent(Player1, 'x')
    tictactoe.add_agent(Player2, 'o')

    while not tictactoe.game_has_ended()[0]:
        next_move1 = Player1.emit_move()
        tictactoe.move(next_move1)
        if not tictactoe.game_has_ended()[0]:
            next_move2 = Player2.emit_move()
            tictactoe.move(next_move2)

    if args.verbose:
        who_won = tictactoe.game_has_ended()[1]
        if who_won == 'draw':
            print("Draw!")
        elif who_won == 'x':
            print("Won!")
        elif who_won == 'o':
            print('Lost!')
        else:
            print("Couldn't determine... Future unclear")
