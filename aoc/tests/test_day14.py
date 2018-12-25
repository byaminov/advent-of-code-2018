import unittest

from aoc.day14 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual('5158916779', solve1(9))
        self.assertEqual('0124515891', solve1(5))
        self.assertEqual('9251071085', solve1(18))
        print('Solving 1')
        self.assertEqual('6107101544', solve1(110201))

    def test_solve2(self):
        self.assertEqual(9, solve2(51589))
        self.assertEqual(18, solve2(92510))
        print('Solving 2')
        self.assertEqual(20291131, solve2(110201))
