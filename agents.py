#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import os

from random import choice, uniform
from tictactoe import TicTacToe


class TicTacToeAgent:
    def __init__(self, board):
        pass

    def emit_move(self):
        pass

    def notify_game_ended(self, won: bool):
        pass


class HumanTicTacToeAgent(TicTacToeAgent):
    """
    A tictactoe agent that asks for input
    """

    def __init__(self, board):
        self.playing_board = board

    def emit_move(self):
        move = input("Make a move: ")
        move_x, move_y = move.split(" ")
        return (int(move_x), int(move_y))

    def notify_game_ended(self, won: bool):
        pass


class RandomTicTacToeAgent(TicTacToeAgent):
    """
    A tictactoe agent that makes random moves
    """

    def __init__(self, board):
        self.playing_board = board

    def emit_move(self):
        return choice(self.playing_board.get_valid_moves())

    def notify_game_ended(self, won: bool):
        pass


class RLTicTacToeAgent(TicTacToeAgent):
    """
    A tictactoe agent that makes moves according to a reinforcement learning algorithm
    """

    def __init__(self, board, moves_dict):
        self.playing_board = board
        self.moves_dict = moves_dict
        self.exploration_rate = 0.33
        self.visited_states = []
        self.reward = 1.0

    def emit_move(self):

        valid_moves = self.playing_board.get_valid_moves()

        if uniform(0, 1) <= self.exploration_rate:
            chosen_move = choice(valid_moves)
            visited = TicTacToe(self.playing_board.get_state())
            visited.move(chosen_move)
            next_state = visited.get_state()
            self.visited_states.append(next_state)
            if next_state not in self.moves_dict.keys():
                self.moves_dict.update({next_state: 0.5})
            return chosen_move
        else:
            considering_moves = []
            for move in valid_moves:
                next_board = TicTacToe(self.playing_board.get_state())
                next_board.move(move)
                next_state = next_board.get_state()

                if next_board.game_has_ended():
                    self.moves_dict.update({next_state: 1})
                    considering_moves.append({move: 1.0})
                elif next_state in self.moves_dict.keys():
                    considering_moves.append({move: self.moves_dict[next_state]})
                else:
                    self.moves_dict.update({next_state: 0.5})
                    considering_moves.append({move: 0.5})

            sorted_list = list(
                reversed(
                    sorted(considering_moves, key=lambda dict: list(dict.values())[0])
                )
            )
            chosen_move = list(sorted_list[0].keys())[0]
            next_board = TicTacToe(self.playing_board.get_state())
            next_board.move(chosen_move)
            next_state = next_board.get_state()
            self.visited_states.append(next_state)

            return chosen_move

    def notify_game_ended(self, won: bool):
        reward = self.reward / len(self.visited_states) if won else -(self.reward /len(self.visited_states))
        for visited in self.visited_states:
            if self.moves_dict[visited] + reward > 0 and self.moves_dict[visited] + reward < 1:
                self.moves_dict[visited] += reward
            else:
                if reward < 0:
                    self.moves_dict[visited] = 0.0
                else:
                    self.moves_dict[visited] = 1.0
