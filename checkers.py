#!/usr/bin/env python
# -*- coding: utf-8 -*-

from random import choice



class CheckersAgent:
    
    def __init__(self, board: Checkers):
        pass
    
    def emit_move(self):
        pass
    

class HumanCheckersAgent(CheckersAgent):
    '''
    A checkers agent that asks for input
    '''
    
    def __init__(self, board: Checkers):
        self.playing_board = board
        
    def emit_move(self):
        move = input("Make a move: ")
        move_x, move_y = move.split(' ')
        return (int(move_x), int(move_y))


class RandomCheckersAgent(CheckersAgent):
    '''
    A checkers agent that makes random moves
    '''
    def __init__(self, board: Checkers):
        self.playing_board = board
        
    def emit_move(self):
        print("Making random move: ")
        return choice(self.playing_board.get_valid_moves())
    
    
class RLCheckersAgent(CheckersAgent):
    '''
    A checkers agent that makes moves according to a reinforcement learning algorithm
    '''
    
    def __init__(self, board: Checkers, moves_dict):
        self.playing_board = board
        self.moves_dict = moves_dict
        self.exploration_rate = 0.1
    
    def emit_move(self):
        pass



class Checkers:
    
    def __init__(self):
        self.board = [
            ['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']
        ]
        
        self.to_move = 'o'
        
    def __repr__(self):
        string = ''
        for i in self.board:
            for j in i:
                string += j
            string += '\n'
        return string
    
    def get_state(self):
        result = ""
        for i in self.board:
            empty_counter = 0
            for j in i:
                if j == '.':
                    empty_counter += 1
                else:
                    if empty_counter != 0:
                        result += str(empty_counter)
                        empty_counter = 0
                    result += j
            if empty_counter != 0:
                result += str(empty_counter)
            
            result += '/'
        return result[0:len(result)-1]
                
    

    def move(self, move: tuple):
        x, y = move
        self.board[x][y] = self.to_move
        self.to_move = 'o' if self.to_move == 'x' else 'x'
        
    
    def get_valid_moves(self):
        valid_moves = []
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == '.':
                    valid_moves.append((x,y))
        return valid_moves
             

    def game_has_ended(self):
        
        # Horizontal win
        if ['x', 'x', 'x'] in self.board:
            return (True, 'x')
        elif ['o', 'o', 'o'] in self.board:
            return (True, 'o')
        
        # Vertical win
        for i in range(3):
            if self.board[i][0]
        
        # Diagonal win
        if self.board[0][0] != '.' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return (True, self.board[0][0])
        elif self.board[0][2] != '.' and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return (True, self.board[0][2])
        
        # Draw
        draw = True
        for i in self.board:
            for j in i:
                if j == '.':
                    draw = False

        return (draw, 'draw')
        


checkers = Checkers()

Player1 = HumanCheckersAgent(checkers)
Player2 = RandomCheckersAgent(checkers)
Player3 = RLCheckersAgent(checkers)

while True:
    print(checkers)
    print(checkers.get_state())
    print("Player1: ")
    player1_move = Player1.emit_move()
    checkers.move(player1_move)
    
    has_ended, player = checkers.game_has_ended()
    if has_ended:
        if player == 'draw':
            print('Draw!')
        else:
            print('Player ' + player + ' won!')
        break
        
    print(checkers)
    print("Player2: ")
    player2_move = Player2.emit_move()
    checkers.move(player2_move)
    
    has_ended, player = checkers.game_has_ended()
    if has_ended:
        if player == 'draw':
            print('Draw!')
        else:
            print('Player ' + player + ' won!')
        break
