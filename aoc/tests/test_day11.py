import unittest

from aoc.day11 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(4, power(3, 5, 8))
        self.assertEqual(-5, power(122, 79, 57))
        self.assertEqual(4, power(101, 153, 71))
        self.assertEqual((33, 45), solve1(18))
        print('Solving 1')
        self.assertEqual((20, 43), solve1(1309))

    def test_solve2(self):
        self.assertEqual((90, 269, 16), solve2(18))
        self.assertEqual((232, 251, 12), solve2(42))
        print('Solving 2')
        self.assertEqual((233, 271, 13), solve2(1309))
