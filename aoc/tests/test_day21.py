import unittest

from aoc.day21 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        print('Solving 1')
        self.assertEqual(4682012, solve1())

    def test_solve2(self):
        print('Solving 2')
        self.assertEqual(5363733, solve2())


text = '''#ip 4
seti 123 0 1
bani 1 456 1
eqri 1 72 1
addr 1 4 4
seti 0 0 4
seti 0 7 1
bori 1 65536 2
seti 8725355 6 1
bani 2 255 5
addr 1 5 1
bani 1 16777215 1
muli 1 65899 1
bani 1 16777215 1
gtir 256 2 5
addr 5 4 4
addi 4 1 4
seti 27 8 4
seti 0 0 5
addi 5 1 3
muli 3 256 3
gtrr 3 2 3
addr 3 4 4
addi 4 1 4
seti 25 1 4
addi 5 1 5
seti 17 9 4
setr 5 1 2
seti 7 6 4
eqrr 1 0 5
addr 5 4 4
seti 5 7 4'''
