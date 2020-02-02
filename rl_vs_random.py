#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tictactoe import TicTacToe
from agents import RLTicTacToeAgent, RandomTicTacToeAgent


state_dict = {}

tictactoe = TicTacToe()

Player1 = RLTicTacToeAgent(tictactoe, state_dict)
Player2 = RandomTicTacToeAgent(tictactoe)

tictactoe.add_agent(Player1, 'o')
tictactoe.add_agent(Player2, 'x')

while not tictactoe.game_has_ended()[0]:
    next_move1 = Player1.emit_move()
    tictactoe.move(next_move1)
    if not tictactoe.game_has_ended()[0]:
        next_move2 = Player2.emit_move()
        tictactoe.move(next_move2)
