import unittest

from aoc.day22 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        print('Testing')
        self.assertEqual(114, solve1(depth=510, target=(10, 10)))
        print('Solving 1')
        self.assertEqual(7915, solve1(depth=depth, target=target))

    def test_solve2(self):
        print('Testing')
        self.assertEqual(45, solve2(depth=510, target=(10, 10)))
        print('Solving 2')
        self.assertEqual(980, solve2(depth=depth, target=target))


depth = 3339
target = (10, 715)

