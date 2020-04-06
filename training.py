#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle
import argparse
import sys
import signal

from tictactoe import TicTacToe
from agents import RLTicTacToeAgent, RandomTicTacToeAgent


parser = argparse.ArgumentParser(description='Train a tic tac toe agent')

parser.add_argument('--file1', type=str,
                    help='The data file to keep the agents state')
parser.add_argument('--file2', type=str,
                    help='The data file to keep the agents state')
parser.add_argument('--verbose', action='store_const',
                    const=True, default=False,
                    help='Print result of the game')
parser.add_argument('-n', type=int, default=1, help='Number of games to play')
args = parser.parse_args()


def signal_handler(sig, frame):
    if args.file1:
        with open(args.file1, 'wb') as fp:
            pickle.dump(state_dict1, fp, protocol=pickle.HIGHEST_PROTOCOL)
    if args.file2:
        with open(args.file2, 'wb') as fp:
            pickle.dump(state_dict2, fp, protocol=pickle.HIGHEST_PROTOCOL)
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

state_dict1 = {}
state_dict2 = {}

if args.file1:
    if os.path.exists(args.file1):
        with open(args.file1, 'rb') as fp:
            state_dict1 = pickle.load(fp)
    else:
        state_dict1 = {}

if args.file2:
    if os.path.exists(args.file2):
        with open(args.file2, 'rb') as fp:
            state_dict2 = pickle.load(fp)
    else:
        state_dict2 = {}


for i in range(args.n):

    tictactoe = TicTacToe()

    Player1 = RLTicTacToeAgent(tictactoe, state_dict1)
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

    for ag in [Player1]:
        if ag.exploration_rate > 0.1:
            ag.exploration_rate -= 0.001

if args.file1:
    with open(args.file1, 'wb') as fp:
        pickle.dump(state_dict1, fp, protocol=pickle.HIGHEST_PROTOCOL)
if args.file2:
    with open(args.file2, 'wb') as fp:
        pickle.dump(state_dict2, fp, protocol=pickle.HIGHEST_PROTOCOL)
