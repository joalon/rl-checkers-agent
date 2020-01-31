#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from checkers import Checkers


class TestCheckers(unittest.TestCase):

    def test_diagonal_win(self):

        checkers = Checkers()

        checkers.move((0,0))
        checkers.move((0,1))
        checkers.move((1,1))
        checkers.move((1,0))
        checkers.move((2,2))

        self.assertEqual(checkers.game_has_ended(), (True, 'o'))

    def test_horizontal_win(self):

        checkers = Checkers()

        checkers.move((0,0))
        checkers.move((1,1))
        checkers.move((0,1))
        checkers.move((1,2))
        checkers.move((0,2))

        self.assertEqual(checkers.game_has_ended(), (True, 'o'))




if __name__ == '__main__':
    unittest.main()
