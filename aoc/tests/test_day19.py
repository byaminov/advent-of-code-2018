import unittest

from aoc.day19 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        print('Testing')
        self.assertEqual(6, solve1('''#ip 0
seti 5 0 1
seti 6 0 2
addi 0 1 0
addr 1 2 3
setr 1 0 0
seti 8 0 4
seti 9 0 5'''))
        print('Solving 1')
        self.assertEqual(1120, solve1(text))

    def test_solve2(self):
        print('Solving 2')
        self.assertEqual(12768192, solve2(10551373))


text = '''#ip 5
addi 5 16 5
seti 1 8 2
seti 1 1 1
mulr 2 1 4
eqrr 4 3 4
addr 4 5 5
addi 5 1 5
addr 2 0 0
addi 1 1 1
gtrr 1 3 4
addr 5 4 5
seti 2 8 5
addi 2 1 2
gtrr 2 3 4
addr 4 5 5
seti 1 7 5
mulr 5 5 5
addi 3 2 3
mulr 3 3 3
mulr 5 3 3
muli 3 11 3
addi 4 6 4
mulr 4 5 4
addi 4 5 4
addr 3 4 3
addr 5 0 5
seti 0 0 5
setr 5 3 4
mulr 4 5 4
addr 5 4 4
mulr 5 4 4
muli 4 14 4
mulr 4 5 4
addr 3 4 3
seti 0 3 0
seti 0 0 5'''
