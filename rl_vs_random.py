#!/usr/bin/env python
# -*- coding: utf-8 -*-

from checkers import Checkers
from agents import RLCheckersAgent, RandomCheckersAgent


state_dict = {}

checkers = Checkers()

Player1 = RLCheckersAgent(checkers, state_dict)
Player2 = RandomCheckersAgent(checkers)

for i in range(5):
    next_move1 = Player1.emit_move()
    checkers.move(next_move1)
    next_move2 = Player2.emit_move()
    checkers.move(next_move2)
