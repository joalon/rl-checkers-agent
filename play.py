#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoe import TicTacToe
from agents import HumanTicTacToeAgent, RandomTicTacToeAgent, RLTicTacToeAgent

tictactoe = TicTacToe()

rl_dict = {}

Player1 = HumanTicTacToeAgent(tictactoe)
Player2 = RandomTicTacToeAgent(tictactoe)
Player3 = RLTicTacToeAgent(tictactoe, rl_dict)

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


