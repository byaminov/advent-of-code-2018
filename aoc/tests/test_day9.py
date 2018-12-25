import unittest

from aoc.day9 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(32, solve1(n_players=9, last_marble_worth=25))
        self.assertEqual(8317, solve1(n_players=10, last_marble_worth=1618))
        self.assertEqual(146373, solve1(n_players=13, last_marble_worth=7999))
        self.assertEqual(2764, solve1(n_players=17, last_marble_worth=1104))
        self.assertEqual(54718, solve1(n_players=21, last_marble_worth=6111))
        self.assertEqual(37305, solve1(n_players=30, last_marble_worth=5807))

        print('Solving 1')
        self.assertEqual(367634, solve1(n_players=479, last_marble_worth=71035))

    def test_solve2(self):
        self.assertEqual(32, solve1(n_players=9, last_marble_worth=25))
        self.assertEqual(8317, solve1(n_players=10, last_marble_worth=1618))
        self.assertEqual(8317, solve1(n_players=10, last_marble_worth=1618))
        self.assertEqual(37305, solve1(n_players=30, last_marble_worth=5807))
        print('Solving 2')
        self.assertEqual(3020072891, solve1(n_players=479, last_marble_worth=7103500))
