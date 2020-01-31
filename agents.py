#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice, uniform

from checkers import Checkers


class CheckersAgent:

    def __init__(self, board):
        pass

    def emit_move(self):
        pass

    def notify_game_ended(self):
        pass


class HumanCheckersAgent(CheckersAgent):
    '''
    A checkers agent that asks for input
    '''

    def __init__(self, board):
        self.playing_board = board

    def emit_move(self):
        move = input("Make a move: ")
        move_x, move_y = move.split(' ')
        return (int(move_x), int(move_y))

    def notify_game_ended(self):
        pass


class RandomCheckersAgent(CheckersAgent):
    '''
    A checkers agent that makes random moves
    '''
    def __init__(self, board):
        self.playing_board = board

    def emit_move(self):
        print("Making random move: ")
        return choice(self.playing_board.get_valid_moves())

    def notify_game_ended(self):
        pass


class RLCheckersAgent(CheckersAgent):
    '''
    A checkers agent that makes moves according to a reinforcement learning algorithm
    '''

    def __init__(self, board, moves_dict):
        self.playing_board = board
        self.moves_dict = moves_dict
        self.exploration_rate = 0.1
        self.visited_states = []

    def emit_move(self):

        valid_moves = self.playing_board.get_valid_moves()

        if uniform(0, 1) <= self.exploration_rate:
            chosen_move = choice(valid_moves)
            visited = Checkers(self.playing_board.get_state())
            visited.move(chosen_move)
            self.visited_states.append(visited.get_state())
            return chosen_move
        else:
            considering_moves = []
            for move in valid_moves:
                next_board = Checkers(self.playing_board.get_state())
                next_board.move(move)
                next_state = next_board.get_state()

                if next_state in self.moves_dict:
                    considering_moves.append({move: self.moves_dict[next_state]})
                else:
                    self.moves_dict.update({next_state: 0.5})
                    considering_moves.append({move: 0.5})

            sorted_list = list(reversed(sorted(considering_moves, key=lambda dict: list(dict.values())[0])))

            return list(sorted_list[0].keys())[0]

