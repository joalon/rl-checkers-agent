#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_diagonal_win(self):

        tictactoe = TicTacToe()

        tictactoe.move((0, 0))
        tictactoe.move((0, 1))
        tictactoe.move((1, 1))
        tictactoe.move((1, 0))
        tictactoe.move((2, 2))

        self.assertEqual(tictactoe.game_has_ended(), (True, "x"))

    def test_horizontal_win(self):

        tictactoe = TicTacToe()

        tictactoe.move((0, 0))
        tictactoe.move((1, 1))
        tictactoe.move((0, 1))
        tictactoe.move((1, 2))
        tictactoe.move((0, 2))

        self.assertEqual(tictactoe.game_has_ended(), (True, "x"))


if __name__ == "__main__":
    unittest.main()
