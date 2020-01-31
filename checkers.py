#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Checkers:

    def __init__(self, state: str = None):

        if not state:
            self.board = [
                ['.', '.', '.'],
                ['.', '.', '.'],
                ['.', '.', '.']
            ]

            self.to_move = 'o'
        else:
            self.to_move = 'o' if state.count('x') == state.count('o') else 'x' 

            self.board = []


            new_line = []
           
            for c in state:
                if c == '/':
                    self.board.append(new_line)
                    new_line = []
                elif c.isdigit():
                    for i in range(int(c)):
                        new_line.append('.')
                else:
                    new_line.append(c)
            self.board.append(new_line)

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
            if self.board[i][0] != '.' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return (True, self.board[i][0])
        
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

