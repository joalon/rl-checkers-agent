#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

from tictactoe import TicTacToe
from agents import HumanTicTacToeAgent, RandomTicTacToeAgent, RLTicTacToeAgent

f = 'data.p'
if os.path.exists(f):
    with open(f, 'rb') as fp:
        state_dict = pickle.load(fp)
else:
    state_dict = {}

tictactoe = TicTacToe()

Player1 = HumanTicTacToeAgent(tictactoe)
Player2 = RLTicTacToeAgent(tictactoe, state_dict)

while True:
    print(tictactoe)
    print(tictactoe.get_state())
    print("Player1: ")
    player1_move = Player1.emit_move()
    tictactoe.move(player1_move)

    has_ended, player = tictactoe.game_has_ended()
    if has_ended:
        if player == 'draw':
            print('Draw!')
        else:
            print('Player ' + player + ' won!')
        break

    print(tictactoe)
    print("Player2: ")
    player2_move = Player2.emit_move()
    tictactoe.move(player2_move)

    has_ended, player = tictactoe.game_has_ended()
    if has_ended:
        if player == 'draw':
            print('Draw!')
        else:
            print('Player ' + player + ' won!')
        break


