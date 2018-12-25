import unittest

from aoc.day16 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual((9, {'mulr', 'addi', 'seti'}), find_possible_opcodes([
            'Before: [3, 2, 1, 1]',
            '9 2 1 2',
            'After:  [3, 2, 2, 1]'
        ]))
        print('Solving 1')
        self.assertEqual(590, solve1(text))

    def test_solve2(self):
        print('Solving 2')
        self.assertEqual(475, solve2(text))


text = '''Before: [3, 3, 2, 3]
3 1 2 2
After:  [3, 3, 2, 3]

Before: [1, 3, 0, 1]
12 0 2 3
After:  [1, 3, 0, 0]

Before: [0, 3, 2, 0]
14 2 3 0
After:  [1, 3, 2, 0]

Before: [2, 3, 3, 3]
10 0 3 0
After:  [2, 3, 3, 3]

Before: [0, 1, 2, 0]
7 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 1, 2, 0]
7 1 2 2
After:  [3, 1, 0, 0]

Before: [1, 2, 1, 3]
6 2 2 2
After:  [1, 2, 2, 3]

Before: [1, 3, 2, 3]
3 3 2 3
After:  [1, 3, 2, 2]

Before: [0, 1, 2, 0]
8 0 0 1
After:  [0, 0, 2, 0]

Before: [1, 2, 3, 1]
0 2 3 2
After:  [1, 2, 1, 1]

Before: [3, 2, 2, 1]
9 3 2 3
After:  [3, 2, 2, 1]

Before: [1, 2, 2, 3]
4 0 2 0
After:  [0, 2, 2, 3]

Before: [1, 3, 2, 0]
3 1 2 1
After:  [1, 2, 2, 0]

Before: [3, 0, 0, 3]
1 1 0 1
After:  [3, 0, 0, 3]

Before: [1, 1, 2, 0]
4 0 2 2
After:  [1, 1, 0, 0]

Before: [2, 0, 1, 3]
1 1 0 2
After:  [2, 0, 0, 3]

Before: [3, 2, 2, 1]
9 3 2 2
After:  [3, 2, 1, 1]

Before: [2, 2, 2, 3]
3 3 2 3
After:  [2, 2, 2, 2]

Before: [0, 3, 2, 2]
5 3 1 2
After:  [0, 3, 0, 2]

Before: [2, 0, 2, 1]
9 3 2 3
After:  [2, 0, 2, 1]

Before: [0, 3, 2, 2]
5 3 1 0
After:  [0, 3, 2, 2]

Before: [3, 0, 0, 2]
1 1 0 3
After:  [3, 0, 0, 0]

Before: [1, 3, 2, 2]
11 2 1 1
After:  [1, 0, 2, 2]

Before: [1, 3, 2, 2]
11 2 1 2
After:  [1, 3, 0, 2]

Before: [0, 0, 3, 1]
0 2 3 1
After:  [0, 1, 3, 1]

Before: [2, 2, 2, 1]
9 3 2 1
After:  [2, 1, 2, 1]

Before: [0, 0, 2, 1]
2 2 2 1
After:  [0, 4, 2, 1]

Before: [0, 0, 2, 1]
2 2 2 0
After:  [4, 0, 2, 1]

Before: [2, 3, 0, 2]
15 1 0 2
After:  [2, 3, 2, 2]

Before: [1, 0, 1, 2]
6 2 2 2
After:  [1, 0, 2, 2]

Before: [2, 3, 2, 0]
2 2 2 0
After:  [4, 3, 2, 0]

Before: [1, 3, 3, 2]
5 3 1 3
After:  [1, 3, 3, 0]

Before: [1, 3, 0, 1]
12 0 2 2
After:  [1, 3, 0, 1]

Before: [3, 3, 1, 2]
15 1 3 3
After:  [3, 3, 1, 2]

Before: [0, 1, 1, 0]
13 0 2 1
After:  [0, 0, 1, 0]

Before: [0, 3, 2, 1]
14 2 3 1
After:  [0, 1, 2, 1]

Before: [3, 1, 2, 2]
7 1 2 2
After:  [3, 1, 0, 2]

Before: [2, 1, 2, 3]
2 2 2 1
After:  [2, 4, 2, 3]

Before: [0, 0, 3, 0]
13 0 2 2
After:  [0, 0, 0, 0]

Before: [0, 0, 3, 2]
8 0 0 1
After:  [0, 0, 3, 2]

Before: [2, 2, 2, 2]
2 3 2 3
After:  [2, 2, 2, 4]

Before: [3, 3, 1, 3]
10 2 3 2
After:  [3, 3, 1, 3]

Before: [1, 0, 3, 1]
0 2 3 0
After:  [1, 0, 3, 1]

Before: [3, 0, 1, 2]
15 0 3 1
After:  [3, 2, 1, 2]

Before: [0, 2, 1, 1]
6 2 2 1
After:  [0, 2, 1, 1]

Before: [0, 0, 2, 1]
9 3 2 2
After:  [0, 0, 1, 1]

Before: [0, 2, 1, 2]
13 0 3 0
After:  [0, 2, 1, 2]

Before: [1, 0, 2, 3]
3 3 2 3
After:  [1, 0, 2, 2]

Before: [1, 3, 2, 1]
14 2 3 2
After:  [1, 3, 1, 1]

Before: [0, 0, 2, 1]
9 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 3, 2, 0]
8 0 0 0
After:  [0, 3, 2, 0]

Before: [2, 2, 2, 0]
14 2 3 3
After:  [2, 2, 2, 1]

Before: [3, 3, 2, 3]
11 2 1 2
After:  [3, 3, 0, 3]

Before: [1, 3, 1, 2]
5 3 1 0
After:  [0, 3, 1, 2]

Before: [0, 1, 2, 0]
13 0 1 3
After:  [0, 1, 2, 0]

Before: [1, 3, 1, 2]
5 3 1 3
After:  [1, 3, 1, 0]

Before: [1, 0, 2, 3]
2 2 2 0
After:  [4, 0, 2, 3]

Before: [0, 3, 2, 1]
14 2 3 3
After:  [0, 3, 2, 1]

Before: [0, 3, 2, 0]
11 2 1 2
After:  [0, 3, 0, 0]

Before: [1, 3, 2, 3]
3 1 2 1
After:  [1, 2, 2, 3]

Before: [3, 1, 2, 0]
7 1 2 1
After:  [3, 0, 2, 0]

Before: [0, 1, 0, 3]
13 0 3 0
After:  [0, 1, 0, 3]

Before: [0, 3, 2, 1]
11 2 1 3
After:  [0, 3, 2, 0]

Before: [0, 2, 2, 1]
9 3 2 0
After:  [1, 2, 2, 1]

Before: [3, 1, 2, 1]
9 3 2 1
After:  [3, 1, 2, 1]

Before: [3, 2, 0, 2]
1 2 0 3
After:  [3, 2, 0, 0]

Before: [3, 3, 3, 2]
5 3 1 2
After:  [3, 3, 0, 2]

Before: [3, 0, 1, 3]
1 1 0 2
After:  [3, 0, 0, 3]

Before: [1, 1, 2, 2]
7 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 2]
7 1 2 1
After:  [3, 0, 2, 2]

Before: [3, 1, 0, 1]
1 2 0 3
After:  [3, 1, 0, 0]

Before: [1, 2, 2, 2]
4 0 2 3
After:  [1, 2, 2, 0]

Before: [1, 2, 0, 0]
12 0 2 1
After:  [1, 0, 0, 0]

Before: [0, 2, 2, 1]
2 1 2 3
After:  [0, 2, 2, 4]

Before: [0, 0, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [0, 0, 2, 1]
14 2 3 3
After:  [0, 0, 2, 1]

Before: [2, 3, 2, 1]
11 2 1 1
After:  [2, 0, 2, 1]

Before: [2, 0, 1, 1]
1 1 0 2
After:  [2, 0, 0, 1]

Before: [2, 3, 1, 2]
6 2 2 0
After:  [2, 3, 1, 2]

Before: [2, 3, 2, 2]
11 2 1 0
After:  [0, 3, 2, 2]

Before: [3, 2, 2, 0]
2 1 2 2
After:  [3, 2, 4, 0]

Before: [0, 3, 1, 3]
13 0 1 2
After:  [0, 3, 0, 3]

Before: [0, 3, 2, 1]
11 2 1 1
After:  [0, 0, 2, 1]

Before: [2, 3, 2, 2]
5 3 1 2
After:  [2, 3, 0, 2]

Before: [2, 3, 2, 1]
15 1 0 1
After:  [2, 2, 2, 1]

Before: [2, 3, 2, 3]
11 2 1 2
After:  [2, 3, 0, 3]

Before: [0, 1, 2, 3]
7 1 2 1
After:  [0, 0, 2, 3]

Before: [0, 1, 3, 2]
13 0 2 2
After:  [0, 1, 0, 2]

Before: [3, 3, 2, 2]
3 0 2 3
After:  [3, 3, 2, 2]

Before: [2, 0, 2, 1]
9 3 2 2
After:  [2, 0, 1, 1]

Before: [0, 0, 2, 0]
14 2 3 0
After:  [1, 0, 2, 0]

Before: [3, 1, 2, 1]
7 1 2 1
After:  [3, 0, 2, 1]

Before: [0, 2, 2, 1]
14 2 3 1
After:  [0, 1, 2, 1]

Before: [1, 2, 2, 3]
10 1 3 3
After:  [1, 2, 2, 2]

Before: [3, 1, 2, 3]
3 3 2 0
After:  [2, 1, 2, 3]

Before: [0, 2, 2, 2]
8 0 0 2
After:  [0, 2, 0, 2]

Before: [0, 2, 2, 3]
8 0 0 3
After:  [0, 2, 2, 0]

Before: [0, 1, 0, 2]
8 0 0 2
After:  [0, 1, 0, 2]

Before: [1, 3, 2, 1]
9 3 2 3
After:  [1, 3, 2, 1]

Before: [3, 0, 2, 1]
14 2 3 2
After:  [3, 0, 1, 1]

Before: [1, 0, 2, 1]
2 2 2 2
After:  [1, 0, 4, 1]

Before: [0, 3, 0, 2]
5 3 1 0
After:  [0, 3, 0, 2]

Before: [3, 1, 2, 3]
7 1 2 1
After:  [3, 0, 2, 3]

Before: [2, 3, 2, 2]
11 2 1 1
After:  [2, 0, 2, 2]

Before: [3, 0, 2, 2]
3 0 2 0
After:  [2, 0, 2, 2]

Before: [1, 2, 2, 0]
4 0 2 0
After:  [0, 2, 2, 0]

Before: [1, 3, 0, 2]
5 3 1 0
After:  [0, 3, 0, 2]

Before: [1, 1, 2, 2]
7 1 2 2
After:  [1, 1, 0, 2]

Before: [0, 2, 0, 0]
8 0 0 1
After:  [0, 0, 0, 0]

Before: [3, 3, 2, 1]
11 2 1 0
After:  [0, 3, 2, 1]

Before: [3, 3, 1, 2]
5 3 1 0
After:  [0, 3, 1, 2]

Before: [3, 2, 3, 3]
15 0 1 0
After:  [2, 2, 3, 3]

Before: [1, 1, 2, 3]
3 3 2 0
After:  [2, 1, 2, 3]

Before: [2, 0, 2, 1]
1 1 0 1
After:  [2, 0, 2, 1]

Before: [1, 0, 0, 1]
12 0 2 3
After:  [1, 0, 0, 0]

Before: [3, 2, 2, 0]
3 0 2 0
After:  [2, 2, 2, 0]

Before: [1, 1, 0, 0]
12 0 2 2
After:  [1, 1, 0, 0]

Before: [1, 3, 3, 2]
5 3 1 1
After:  [1, 0, 3, 2]

Before: [2, 1, 2, 1]
9 3 2 1
After:  [2, 1, 2, 1]

Before: [2, 0, 2, 3]
15 3 0 2
After:  [2, 0, 2, 3]

Before: [2, 0, 2, 1]
9 3 2 1
After:  [2, 1, 2, 1]

Before: [3, 3, 2, 0]
2 2 2 1
After:  [3, 4, 2, 0]

Before: [3, 2, 2, 2]
15 0 3 3
After:  [3, 2, 2, 2]

Before: [0, 2, 3, 1]
13 0 3 3
After:  [0, 2, 3, 0]

Before: [1, 1, 2, 0]
4 0 2 0
After:  [0, 1, 2, 0]

Before: [2, 2, 2, 0]
0 2 1 3
After:  [2, 2, 2, 0]

Before: [0, 3, 2, 2]
11 2 1 2
After:  [0, 3, 0, 2]

Before: [1, 3, 2, 1]
4 0 2 3
After:  [1, 3, 2, 0]

Before: [3, 0, 2, 0]
1 1 0 1
After:  [3, 0, 2, 0]

Before: [3, 1, 1, 2]
15 0 3 1
After:  [3, 2, 1, 2]

Before: [1, 0, 2, 1]
4 0 2 1
After:  [1, 0, 2, 1]

Before: [2, 0, 1, 0]
6 2 2 1
After:  [2, 2, 1, 0]

Before: [3, 1, 2, 3]
3 0 2 3
After:  [3, 1, 2, 2]

Before: [3, 0, 3, 1]
0 2 3 3
After:  [3, 0, 3, 1]

Before: [0, 2, 2, 1]
2 1 2 1
After:  [0, 4, 2, 1]

Before: [1, 3, 1, 2]
6 2 2 2
After:  [1, 3, 2, 2]

Before: [3, 1, 2, 0]
14 2 3 2
After:  [3, 1, 1, 0]

Before: [1, 0, 2, 2]
4 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 3, 2, 1]
9 3 2 2
After:  [3, 3, 1, 1]

Before: [1, 3, 2, 2]
5 3 1 1
After:  [1, 0, 2, 2]

Before: [1, 2, 2, 1]
4 0 2 0
After:  [0, 2, 2, 1]

Before: [0, 2, 2, 2]
0 2 1 0
After:  [0, 2, 2, 2]

Before: [0, 0, 3, 3]
8 0 0 0
After:  [0, 0, 3, 3]

Before: [1, 2, 1, 2]
6 2 2 3
After:  [1, 2, 1, 2]

Before: [1, 2, 0, 0]
12 0 2 0
After:  [0, 2, 0, 0]

Before: [2, 3, 2, 1]
11 2 1 0
After:  [0, 3, 2, 1]

Before: [3, 2, 2, 3]
15 3 1 2
After:  [3, 2, 2, 3]

Before: [3, 1, 0, 2]
1 2 0 0
After:  [0, 1, 0, 2]

Before: [0, 2, 1, 0]
8 0 0 2
After:  [0, 2, 0, 0]

Before: [1, 2, 2, 2]
2 2 2 1
After:  [1, 4, 2, 2]

Before: [2, 1, 2, 3]
15 3 0 1
After:  [2, 2, 2, 3]

Before: [2, 0, 2, 3]
1 1 0 3
After:  [2, 0, 2, 0]

Before: [0, 2, 2, 0]
0 2 1 0
After:  [0, 2, 2, 0]

Before: [1, 2, 2, 1]
14 2 3 1
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 3]
7 1 2 2
After:  [1, 1, 0, 3]

Before: [0, 1, 1, 0]
6 2 2 0
After:  [2, 1, 1, 0]

Before: [3, 3, 0, 2]
5 3 1 3
After:  [3, 3, 0, 0]

Before: [3, 3, 1, 3]
6 2 2 3
After:  [3, 3, 1, 2]

Before: [2, 3, 2, 0]
3 1 2 0
After:  [2, 3, 2, 0]

Before: [0, 3, 3, 1]
8 0 0 0
After:  [0, 3, 3, 1]

Before: [0, 2, 1, 1]
6 2 2 2
After:  [0, 2, 2, 1]

Before: [0, 3, 2, 3]
3 3 2 0
After:  [2, 3, 2, 3]

Before: [2, 1, 2, 0]
7 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 1, 2, 2]
4 0 2 0
After:  [0, 1, 2, 2]

Before: [1, 3, 3, 1]
0 2 3 3
After:  [1, 3, 3, 1]

Before: [3, 1, 3, 1]
0 2 3 1
After:  [3, 1, 3, 1]

Before: [1, 1, 0, 2]
12 0 2 1
After:  [1, 0, 0, 2]

Before: [0, 3, 3, 3]
8 0 0 3
After:  [0, 3, 3, 0]

Before: [2, 0, 3, 0]
1 1 0 3
After:  [2, 0, 3, 0]

Before: [2, 1, 2, 1]
14 2 3 0
After:  [1, 1, 2, 1]

Before: [2, 1, 2, 0]
7 1 2 1
After:  [2, 0, 2, 0]

Before: [2, 3, 3, 3]
10 0 3 1
After:  [2, 2, 3, 3]

Before: [3, 2, 0, 3]
15 0 1 0
After:  [2, 2, 0, 3]

Before: [2, 2, 2, 0]
0 2 1 0
After:  [0, 2, 2, 0]

Before: [2, 0, 1, 3]
1 1 0 3
After:  [2, 0, 1, 0]

Before: [3, 1, 0, 2]
1 2 0 1
After:  [3, 0, 0, 2]

Before: [3, 0, 2, 1]
9 3 2 1
After:  [3, 1, 2, 1]

Before: [3, 3, 2, 0]
3 0 2 3
After:  [3, 3, 2, 2]

Before: [2, 0, 2, 1]
2 2 2 0
After:  [4, 0, 2, 1]

Before: [0, 1, 0, 1]
8 0 0 2
After:  [0, 1, 0, 1]

Before: [3, 0, 2, 0]
2 2 2 1
After:  [3, 4, 2, 0]

Before: [1, 3, 2, 2]
11 2 1 0
After:  [0, 3, 2, 2]

Before: [1, 0, 0, 0]
12 0 2 2
After:  [1, 0, 0, 0]

Before: [3, 1, 2, 2]
2 3 2 2
After:  [3, 1, 4, 2]

Before: [0, 0, 2, 2]
2 3 2 3
After:  [0, 0, 2, 4]

Before: [2, 3, 2, 3]
3 1 2 3
After:  [2, 3, 2, 2]

Before: [2, 3, 1, 3]
10 2 3 3
After:  [2, 3, 1, 1]

Before: [3, 2, 2, 3]
3 3 2 0
After:  [2, 2, 2, 3]

Before: [2, 0, 1, 0]
6 2 2 2
After:  [2, 0, 2, 0]

Before: [1, 2, 2, 0]
4 0 2 3
After:  [1, 2, 2, 0]

Before: [3, 3, 1, 2]
5 3 1 3
After:  [3, 3, 1, 0]

Before: [3, 2, 2, 1]
9 3 2 1
After:  [3, 1, 2, 1]

Before: [2, 0, 1, 3]
6 2 2 1
After:  [2, 2, 1, 3]

Before: [0, 1, 3, 2]
8 0 0 3
After:  [0, 1, 3, 0]

Before: [1, 3, 0, 2]
12 0 2 0
After:  [0, 3, 0, 2]

Before: [3, 0, 3, 1]
0 2 3 1
After:  [3, 1, 3, 1]

Before: [0, 3, 3, 2]
5 3 1 3
After:  [0, 3, 3, 0]

Before: [0, 0, 3, 2]
8 0 0 2
After:  [0, 0, 0, 2]

Before: [3, 2, 2, 3]
0 2 1 0
After:  [0, 2, 2, 3]

Before: [2, 3, 2, 0]
2 0 2 1
After:  [2, 4, 2, 0]

Before: [0, 1, 1, 2]
8 0 0 1
After:  [0, 0, 1, 2]

Before: [3, 0, 2, 1]
3 0 2 2
After:  [3, 0, 2, 1]

Before: [3, 2, 2, 3]
15 3 1 1
After:  [3, 2, 2, 3]

Before: [1, 2, 2, 0]
0 2 1 3
After:  [1, 2, 2, 0]

Before: [3, 2, 1, 1]
6 2 2 3
After:  [3, 2, 1, 2]

Before: [0, 0, 2, 1]
13 0 2 0
After:  [0, 0, 2, 1]

Before: [0, 0, 1, 1]
6 2 2 0
After:  [2, 0, 1, 1]

Before: [0, 1, 3, 3]
13 0 2 2
After:  [0, 1, 0, 3]

Before: [2, 2, 0, 3]
10 1 3 0
After:  [2, 2, 0, 3]

Before: [2, 2, 2, 3]
2 1 2 1
After:  [2, 4, 2, 3]

Before: [2, 2, 2, 0]
14 2 3 0
After:  [1, 2, 2, 0]

Before: [0, 3, 3, 1]
8 0 0 3
After:  [0, 3, 3, 0]

Before: [2, 2, 2, 1]
9 3 2 3
After:  [2, 2, 2, 1]

Before: [1, 3, 1, 2]
6 2 2 3
After:  [1, 3, 1, 2]

Before: [1, 1, 1, 1]
6 2 2 3
After:  [1, 1, 1, 2]

Before: [0, 2, 2, 1]
2 2 2 3
After:  [0, 2, 2, 4]

Before: [1, 3, 2, 2]
4 0 2 0
After:  [0, 3, 2, 2]

Before: [1, 3, 1, 3]
6 2 2 3
After:  [1, 3, 1, 2]

Before: [0, 1, 1, 2]
13 0 2 1
After:  [0, 0, 1, 2]

Before: [3, 2, 2, 3]
3 0 2 1
After:  [3, 2, 2, 3]

Before: [1, 3, 3, 3]
10 0 3 3
After:  [1, 3, 3, 1]

Before: [0, 0, 1, 0]
6 2 2 1
After:  [0, 2, 1, 0]

Before: [0, 3, 3, 1]
8 0 0 2
After:  [0, 3, 0, 1]

Before: [2, 1, 0, 3]
15 3 0 1
After:  [2, 2, 0, 3]

Before: [1, 0, 0, 3]
12 0 2 0
After:  [0, 0, 0, 3]

Before: [1, 0, 0, 3]
12 0 2 2
After:  [1, 0, 0, 3]

Before: [2, 3, 2, 2]
5 3 1 1
After:  [2, 0, 2, 2]

Before: [1, 0, 0, 2]
12 0 2 0
After:  [0, 0, 0, 2]

Before: [0, 2, 1, 1]
6 2 2 0
After:  [2, 2, 1, 1]

Before: [0, 0, 1, 2]
8 0 0 2
After:  [0, 0, 0, 2]

Before: [0, 3, 2, 3]
13 0 1 2
After:  [0, 3, 0, 3]

Before: [3, 1, 2, 1]
9 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 3]
4 0 2 1
After:  [1, 0, 2, 3]

Before: [1, 0, 0, 2]
12 0 2 3
After:  [1, 0, 0, 0]

Before: [2, 2, 0, 3]
15 3 1 2
After:  [2, 2, 2, 3]

Before: [0, 0, 3, 2]
13 0 3 1
After:  [0, 0, 3, 2]

Before: [1, 0, 2, 2]
4 0 2 2
After:  [1, 0, 0, 2]

Before: [1, 2, 1, 1]
6 2 2 3
After:  [1, 2, 1, 2]

Before: [1, 1, 2, 1]
4 0 2 1
After:  [1, 0, 2, 1]

Before: [1, 3, 0, 2]
5 3 1 2
After:  [1, 3, 0, 2]

Before: [3, 2, 0, 1]
1 2 0 3
After:  [3, 2, 0, 0]

Before: [3, 2, 2, 0]
14 2 3 3
After:  [3, 2, 2, 1]

Before: [2, 1, 2, 3]
15 3 0 2
After:  [2, 1, 2, 3]

Before: [2, 3, 2, 0]
14 2 3 2
After:  [2, 3, 1, 0]

Before: [0, 3, 3, 2]
5 3 1 2
After:  [0, 3, 0, 2]

Before: [0, 1, 2, 0]
7 1 2 1
After:  [0, 0, 2, 0]

Before: [3, 3, 2, 0]
3 1 2 2
After:  [3, 3, 2, 0]

Before: [2, 1, 2, 3]
7 1 2 0
After:  [0, 1, 2, 3]

Before: [1, 2, 2, 1]
4 0 2 2
After:  [1, 2, 0, 1]

Before: [0, 2, 3, 0]
8 0 0 2
After:  [0, 2, 0, 0]

Before: [2, 3, 2, 0]
11 2 1 3
After:  [2, 3, 2, 0]

Before: [2, 2, 2, 0]
2 0 2 0
After:  [4, 2, 2, 0]

Before: [1, 0, 2, 2]
2 3 2 1
After:  [1, 4, 2, 2]

Before: [0, 3, 1, 2]
13 0 2 2
After:  [0, 3, 0, 2]

Before: [1, 1, 2, 1]
4 0 2 0
After:  [0, 1, 2, 1]

Before: [0, 2, 1, 2]
8 0 0 2
After:  [0, 2, 0, 2]

Before: [3, 0, 2, 1]
9 3 2 0
After:  [1, 0, 2, 1]

Before: [1, 2, 2, 1]
4 0 2 1
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 1]
14 2 3 2
After:  [0, 1, 1, 1]

Before: [1, 0, 2, 1]
2 2 2 1
After:  [1, 4, 2, 1]

Before: [1, 0, 2, 3]
4 0 2 1
After:  [1, 0, 2, 3]

Before: [3, 0, 0, 2]
15 0 3 3
After:  [3, 0, 0, 2]

Before: [2, 2, 2, 1]
9 3 2 0
After:  [1, 2, 2, 1]

Before: [1, 3, 3, 2]
5 3 1 0
After:  [0, 3, 3, 2]

Before: [2, 0, 3, 1]
0 2 3 2
After:  [2, 0, 1, 1]

Before: [3, 3, 0, 2]
15 1 3 1
After:  [3, 2, 0, 2]

Before: [1, 3, 3, 2]
5 3 1 2
After:  [1, 3, 0, 2]

Before: [0, 3, 1, 3]
6 2 2 3
After:  [0, 3, 1, 2]

Before: [1, 1, 2, 0]
7 1 2 0
After:  [0, 1, 2, 0]

Before: [3, 1, 1, 3]
6 2 2 1
After:  [3, 2, 1, 3]

Before: [3, 3, 0, 2]
5 3 1 1
After:  [3, 0, 0, 2]

Before: [0, 1, 1, 1]
13 0 1 1
After:  [0, 0, 1, 1]

Before: [0, 3, 2, 2]
5 3 1 3
After:  [0, 3, 2, 0]

Before: [0, 1, 2, 1]
7 1 2 2
After:  [0, 1, 0, 1]

Before: [0, 0, 2, 1]
8 0 0 1
After:  [0, 0, 2, 1]

Before: [1, 1, 3, 3]
10 0 3 2
After:  [1, 1, 1, 3]

Before: [0, 0, 1, 1]
8 0 0 0
After:  [0, 0, 1, 1]

Before: [1, 3, 3, 2]
15 1 3 3
After:  [1, 3, 3, 2]

Before: [1, 3, 2, 0]
3 1 2 2
After:  [1, 3, 2, 0]

Before: [2, 0, 2, 1]
1 1 0 3
After:  [2, 0, 2, 0]

Before: [3, 0, 0, 2]
1 2 0 3
After:  [3, 0, 0, 0]

Before: [2, 3, 2, 2]
15 1 0 2
After:  [2, 3, 2, 2]

Before: [0, 2, 3, 1]
13 0 2 0
After:  [0, 2, 3, 1]

Before: [2, 0, 3, 2]
1 1 0 1
After:  [2, 0, 3, 2]

Before: [2, 1, 2, 1]
14 2 3 3
After:  [2, 1, 2, 1]

Before: [3, 2, 2, 3]
15 3 1 3
After:  [3, 2, 2, 2]

Before: [1, 0, 2, 1]
4 0 2 2
After:  [1, 0, 0, 1]

Before: [3, 2, 1, 2]
15 0 3 2
After:  [3, 2, 2, 2]

Before: [1, 1, 2, 1]
14 2 3 1
After:  [1, 1, 2, 1]

Before: [0, 3, 2, 1]
9 3 2 3
After:  [0, 3, 2, 1]

Before: [2, 3, 2, 3]
3 3 2 0
After:  [2, 3, 2, 3]

Before: [1, 1, 2, 0]
7 1 2 2
After:  [1, 1, 0, 0]

Before: [0, 0, 0, 1]
13 0 3 0
After:  [0, 0, 0, 1]

Before: [1, 1, 2, 3]
4 0 2 2
After:  [1, 1, 0, 3]

Before: [0, 3, 2, 0]
13 0 2 2
After:  [0, 3, 0, 0]

Before: [3, 1, 2, 1]
9 3 2 2
After:  [3, 1, 1, 1]

Before: [3, 0, 0, 1]
1 2 0 3
After:  [3, 0, 0, 0]

Before: [2, 2, 2, 3]
0 2 1 2
After:  [2, 2, 0, 3]

Before: [0, 0, 3, 1]
8 0 0 2
After:  [0, 0, 0, 1]

Before: [0, 3, 1, 2]
5 3 1 0
After:  [0, 3, 1, 2]

Before: [0, 1, 2, 0]
14 2 3 2
After:  [0, 1, 1, 0]

Before: [0, 3, 2, 3]
3 1 2 1
After:  [0, 2, 2, 3]

Before: [0, 3, 0, 2]
5 3 1 3
After:  [0, 3, 0, 0]

Before: [2, 3, 3, 2]
5 3 1 0
After:  [0, 3, 3, 2]

Before: [0, 0, 3, 1]
8 0 0 0
After:  [0, 0, 3, 1]

Before: [0, 2, 2, 0]
8 0 0 3
After:  [0, 2, 2, 0]

Before: [3, 1, 1, 3]
6 2 2 3
After:  [3, 1, 1, 2]

Before: [0, 3, 3, 0]
8 0 0 0
After:  [0, 3, 3, 0]

Before: [2, 2, 2, 3]
10 1 3 2
After:  [2, 2, 2, 3]

Before: [2, 3, 1, 3]
6 2 2 0
After:  [2, 3, 1, 3]

Before: [2, 3, 2, 3]
3 3 2 2
After:  [2, 3, 2, 3]

Before: [0, 1, 2, 3]
8 0 0 0
After:  [0, 1, 2, 3]

Before: [2, 2, 0, 3]
10 0 3 3
After:  [2, 2, 0, 2]

Before: [3, 0, 0, 3]
1 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 2, 2, 1]
14 2 3 3
After:  [0, 2, 2, 1]

Before: [1, 3, 2, 2]
11 2 1 3
After:  [1, 3, 2, 0]

Before: [3, 2, 1, 2]
15 0 3 3
After:  [3, 2, 1, 2]

Before: [0, 2, 1, 3]
6 2 2 3
After:  [0, 2, 1, 2]

Before: [3, 0, 2, 2]
2 3 2 1
After:  [3, 4, 2, 2]

Before: [3, 1, 0, 0]
1 2 0 0
After:  [0, 1, 0, 0]

Before: [0, 3, 3, 1]
13 0 2 1
After:  [0, 0, 3, 1]

Before: [0, 3, 2, 1]
13 0 3 1
After:  [0, 0, 2, 1]

Before: [0, 3, 2, 1]
9 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 0, 2, 2]
2 2 2 2
After:  [0, 0, 4, 2]

Before: [0, 2, 2, 3]
8 0 0 2
After:  [0, 2, 0, 3]

Before: [1, 2, 2, 2]
4 0 2 1
After:  [1, 0, 2, 2]

Before: [3, 0, 3, 2]
1 1 0 2
After:  [3, 0, 0, 2]

Before: [1, 3, 2, 1]
9 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 1, 1, 2]
13 0 1 2
After:  [0, 1, 0, 2]

Before: [1, 3, 2, 0]
2 2 2 1
After:  [1, 4, 2, 0]

Before: [2, 1, 2, 1]
7 1 2 3
After:  [2, 1, 2, 0]

Before: [2, 0, 2, 3]
3 3 2 1
After:  [2, 2, 2, 3]

Before: [2, 1, 2, 3]
7 1 2 1
After:  [2, 0, 2, 3]

Before: [3, 2, 2, 1]
15 0 1 2
After:  [3, 2, 2, 1]

Before: [1, 2, 2, 3]
4 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 1, 2, 0]
7 1 2 2
After:  [2, 1, 0, 0]

Before: [3, 0, 0, 3]
1 2 0 1
After:  [3, 0, 0, 3]

Before: [3, 2, 2, 0]
3 0 2 3
After:  [3, 2, 2, 2]

Before: [2, 3, 2, 2]
11 2 1 2
After:  [2, 3, 0, 2]

Before: [2, 3, 2, 0]
11 2 1 2
After:  [2, 3, 0, 0]

Before: [1, 1, 1, 3]
10 0 3 3
After:  [1, 1, 1, 1]

Before: [1, 2, 2, 1]
9 3 2 3
After:  [1, 2, 2, 1]

Before: [3, 3, 3, 2]
5 3 1 3
After:  [3, 3, 3, 0]

Before: [0, 2, 2, 1]
9 3 2 1
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 3]
3 3 2 0
After:  [2, 2, 2, 3]

Before: [0, 1, 2, 3]
3 3 2 3
After:  [0, 1, 2, 2]

Before: [2, 2, 3, 1]
0 2 3 3
After:  [2, 2, 3, 1]

Before: [0, 2, 2, 1]
9 3 2 2
After:  [0, 2, 1, 1]

Before: [0, 2, 2, 2]
2 2 2 3
After:  [0, 2, 2, 4]

Before: [3, 0, 1, 1]
6 2 2 3
After:  [3, 0, 1, 2]

Before: [0, 3, 2, 3]
11 2 1 3
After:  [0, 3, 2, 0]

Before: [1, 0, 2, 3]
10 0 3 2
After:  [1, 0, 1, 3]

Before: [1, 1, 2, 1]
9 3 2 0
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 1]
3 1 2 3
After:  [1, 3, 2, 2]

Before: [2, 0, 3, 1]
0 2 3 3
After:  [2, 0, 3, 1]

Before: [1, 0, 2, 0]
4 0 2 3
After:  [1, 0, 2, 0]

Before: [0, 3, 2, 3]
3 1 2 0
After:  [2, 3, 2, 3]

Before: [2, 2, 2, 3]
2 0 2 3
After:  [2, 2, 2, 4]

Before: [2, 3, 3, 3]
10 0 3 3
After:  [2, 3, 3, 2]

Before: [0, 3, 0, 2]
5 3 1 1
After:  [0, 0, 0, 2]

Before: [3, 1, 2, 3]
7 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 0, 2, 3]
2 2 2 1
After:  [0, 4, 2, 3]

Before: [3, 0, 1, 1]
1 1 0 2
After:  [3, 0, 0, 1]

Before: [2, 0, 2, 0]
1 1 0 0
After:  [0, 0, 2, 0]

Before: [1, 0, 0, 0]
12 0 2 0
After:  [0, 0, 0, 0]

Before: [0, 2, 1, 3]
10 1 3 3
After:  [0, 2, 1, 2]

Before: [2, 0, 1, 3]
15 3 0 1
After:  [2, 2, 1, 3]

Before: [2, 3, 1, 2]
5 3 1 0
After:  [0, 3, 1, 2]

Before: [1, 3, 0, 2]
12 0 2 2
After:  [1, 3, 0, 2]

Before: [0, 3, 2, 2]
11 2 1 3
After:  [0, 3, 2, 0]

Before: [3, 0, 0, 1]
1 2 0 2
After:  [3, 0, 0, 1]

Before: [2, 0, 0, 0]
1 1 0 1
After:  [2, 0, 0, 0]

Before: [0, 2, 1, 2]
13 0 1 1
After:  [0, 0, 1, 2]

Before: [1, 1, 2, 0]
4 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 1, 2, 0]
4 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 1, 2, 3]
15 3 0 0
After:  [2, 1, 2, 3]

Before: [2, 0, 0, 1]
1 1 0 2
After:  [2, 0, 0, 1]

Before: [1, 1, 2, 2]
2 3 2 3
After:  [1, 1, 2, 4]

Before: [0, 2, 2, 2]
0 2 1 1
After:  [0, 0, 2, 2]

Before: [1, 2, 0, 2]
12 0 2 3
After:  [1, 2, 0, 0]

Before: [3, 2, 3, 1]
0 2 3 3
After:  [3, 2, 3, 1]

Before: [1, 0, 0, 3]
12 0 2 3
After:  [1, 0, 0, 0]

Before: [1, 2, 2, 0]
4 0 2 2
After:  [1, 2, 0, 0]

Before: [1, 3, 2, 0]
4 0 2 1
After:  [1, 0, 2, 0]

Before: [2, 3, 2, 1]
3 1 2 3
After:  [2, 3, 2, 2]

Before: [2, 1, 2, 0]
14 2 3 3
After:  [2, 1, 2, 1]

Before: [2, 3, 2, 2]
5 3 1 0
After:  [0, 3, 2, 2]

Before: [3, 3, 2, 2]
3 0 2 0
After:  [2, 3, 2, 2]

Before: [0, 3, 2, 3]
3 1 2 3
After:  [0, 3, 2, 2]

Before: [1, 3, 2, 1]
9 3 2 2
After:  [1, 3, 1, 1]

Before: [2, 1, 2, 3]
7 1 2 3
After:  [2, 1, 2, 0]

Before: [0, 3, 2, 1]
3 1 2 2
After:  [0, 3, 2, 1]

Before: [0, 2, 1, 0]
13 0 1 3
After:  [0, 2, 1, 0]

Before: [0, 3, 1, 0]
8 0 0 0
After:  [0, 3, 1, 0]

Before: [1, 0, 0, 3]
10 0 3 0
After:  [1, 0, 0, 3]

Before: [1, 1, 0, 0]
12 0 2 3
After:  [1, 1, 0, 0]

Before: [3, 3, 2, 2]
5 3 1 2
After:  [3, 3, 0, 2]

Before: [0, 3, 2, 3]
13 0 1 3
After:  [0, 3, 2, 0]

Before: [1, 3, 1, 3]
10 2 3 1
After:  [1, 1, 1, 3]

Before: [1, 2, 2, 2]
2 1 2 0
After:  [4, 2, 2, 2]

Before: [0, 3, 2, 3]
3 3 2 2
After:  [0, 3, 2, 3]

Before: [1, 2, 0, 3]
12 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 0, 2, 3]
3 0 2 1
After:  [3, 2, 2, 3]

Before: [0, 1, 3, 0]
13 0 1 1
After:  [0, 0, 3, 0]

Before: [1, 2, 2, 2]
2 3 2 1
After:  [1, 4, 2, 2]

Before: [3, 2, 1, 2]
6 2 2 1
After:  [3, 2, 1, 2]

Before: [2, 3, 1, 3]
10 0 3 0
After:  [2, 3, 1, 3]

Before: [3, 3, 2, 1]
14 2 3 3
After:  [3, 3, 2, 1]

Before: [2, 3, 3, 1]
0 2 3 0
After:  [1, 3, 3, 1]

Before: [1, 1, 0, 2]
12 0 2 0
After:  [0, 1, 0, 2]

Before: [0, 3, 0, 3]
8 0 0 1
After:  [0, 0, 0, 3]

Before: [1, 2, 3, 1]
0 2 3 1
After:  [1, 1, 3, 1]

Before: [2, 1, 2, 0]
14 2 3 2
After:  [2, 1, 1, 0]

Before: [0, 1, 2, 3]
7 1 2 3
After:  [0, 1, 2, 0]

Before: [3, 3, 3, 2]
5 3 1 1
After:  [3, 0, 3, 2]

Before: [2, 3, 2, 3]
11 2 1 1
After:  [2, 0, 2, 3]

Before: [2, 0, 0, 2]
1 1 0 1
After:  [2, 0, 0, 2]

Before: [3, 1, 2, 0]
3 0 2 1
After:  [3, 2, 2, 0]

Before: [1, 1, 2, 1]
7 1 2 3
After:  [1, 1, 2, 0]

Before: [2, 3, 0, 2]
15 1 3 3
After:  [2, 3, 0, 2]

Before: [1, 3, 2, 0]
14 2 3 3
After:  [1, 3, 2, 1]

Before: [3, 3, 2, 0]
14 2 3 3
After:  [3, 3, 2, 1]

Before: [3, 3, 2, 2]
11 2 1 2
After:  [3, 3, 0, 2]

Before: [1, 2, 2, 3]
0 2 1 1
After:  [1, 0, 2, 3]

Before: [3, 2, 3, 3]
10 1 3 2
After:  [3, 2, 2, 3]

Before: [2, 1, 2, 2]
7 1 2 0
After:  [0, 1, 2, 2]

Before: [1, 1, 1, 1]
6 2 2 1
After:  [1, 2, 1, 1]

Before: [3, 1, 2, 2]
3 0 2 3
After:  [3, 1, 2, 2]

Before: [1, 3, 2, 0]
11 2 1 0
After:  [0, 3, 2, 0]

Before: [2, 3, 0, 0]
15 1 0 1
After:  [2, 2, 0, 0]

Before: [3, 3, 3, 2]
5 3 1 0
After:  [0, 3, 3, 2]

Before: [0, 3, 2, 0]
11 2 1 1
After:  [0, 0, 2, 0]

Before: [0, 3, 2, 2]
15 1 3 2
After:  [0, 3, 2, 2]

Before: [0, 1, 2, 1]
13 0 1 1
After:  [0, 0, 2, 1]

Before: [3, 1, 0, 2]
1 2 0 2
After:  [3, 1, 0, 2]

Before: [1, 2, 0, 3]
12 0 2 3
After:  [1, 2, 0, 0]

Before: [3, 3, 1, 0]
6 2 2 3
After:  [3, 3, 1, 2]

Before: [1, 1, 3, 1]
0 2 3 0
After:  [1, 1, 3, 1]

Before: [3, 1, 2, 1]
7 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 1, 1, 3]
6 2 2 2
After:  [0, 1, 2, 3]

Before: [1, 2, 2, 3]
3 3 2 0
After:  [2, 2, 2, 3]

Before: [3, 0, 3, 0]
1 1 0 3
After:  [3, 0, 3, 0]

Before: [1, 0, 2, 1]
4 0 2 3
After:  [1, 0, 2, 0]

Before: [3, 0, 0, 2]
1 1 0 2
After:  [3, 0, 0, 2]

Before: [3, 0, 1, 0]
6 2 2 2
After:  [3, 0, 2, 0]

Before: [0, 2, 2, 3]
3 3 2 0
After:  [2, 2, 2, 3]

Before: [1, 3, 0, 3]
10 0 3 3
After:  [1, 3, 0, 1]

Before: [3, 1, 1, 3]
10 2 3 1
After:  [3, 1, 1, 3]

Before: [0, 1, 2, 3]
2 2 2 1
After:  [0, 4, 2, 3]

Before: [2, 3, 2, 1]
3 1 2 2
After:  [2, 3, 2, 1]

Before: [3, 3, 1, 2]
6 2 2 1
After:  [3, 2, 1, 2]

Before: [3, 0, 2, 3]
3 3 2 2
After:  [3, 0, 2, 3]

Before: [2, 1, 2, 3]
10 0 3 3
After:  [2, 1, 2, 2]

Before: [2, 2, 0, 3]
10 1 3 3
After:  [2, 2, 0, 2]

Before: [3, 3, 2, 0]
14 2 3 1
After:  [3, 1, 2, 0]

Before: [0, 3, 2, 0]
3 1 2 3
After:  [0, 3, 2, 2]

Before: [0, 2, 3, 0]
13 0 1 1
After:  [0, 0, 3, 0]

Before: [0, 2, 2, 2]
13 0 3 0
After:  [0, 2, 2, 2]

Before: [1, 1, 0, 1]
12 0 2 1
After:  [1, 0, 0, 1]

Before: [0, 3, 2, 0]
11 2 1 3
After:  [0, 3, 2, 0]

Before: [2, 1, 2, 1]
7 1 2 2
After:  [2, 1, 0, 1]

Before: [1, 3, 2, 0]
11 2 1 2
After:  [1, 3, 0, 0]

Before: [1, 3, 2, 0]
11 2 1 1
After:  [1, 0, 2, 0]

Before: [3, 0, 2, 1]
14 2 3 3
After:  [3, 0, 2, 1]

Before: [1, 0, 0, 1]
12 0 2 2
After:  [1, 0, 0, 1]

Before: [1, 1, 2, 2]
2 3 2 2
After:  [1, 1, 4, 2]

Before: [1, 1, 2, 1]
14 2 3 2
After:  [1, 1, 1, 1]

Before: [0, 3, 2, 0]
13 0 2 3
After:  [0, 3, 2, 0]

Before: [1, 3, 2, 3]
11 2 1 2
After:  [1, 3, 0, 3]

Before: [2, 1, 2, 3]
15 3 0 3
After:  [2, 1, 2, 2]

Before: [1, 3, 0, 3]
12 0 2 1
After:  [1, 0, 0, 3]

Before: [3, 3, 2, 1]
11 2 1 1
After:  [3, 0, 2, 1]

Before: [0, 3, 3, 3]
13 0 1 2
After:  [0, 3, 0, 3]

Before: [1, 1, 2, 3]
4 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 2, 2, 0]
2 2 2 0
After:  [4, 2, 2, 0]

Before: [1, 0, 2, 2]
4 0 2 3
After:  [1, 0, 2, 0]

Before: [2, 3, 3, 2]
5 3 1 3
After:  [2, 3, 3, 0]

Before: [1, 0, 2, 1]
9 3 2 0
After:  [1, 0, 2, 1]

Before: [0, 3, 3, 0]
13 0 2 0
After:  [0, 3, 3, 0]

Before: [3, 1, 0, 3]
1 2 0 3
After:  [3, 1, 0, 0]

Before: [2, 2, 1, 3]
10 2 3 1
After:  [2, 1, 1, 3]

Before: [3, 1, 2, 0]
3 0 2 2
After:  [3, 1, 2, 0]

Before: [2, 0, 1, 0]
6 2 2 3
After:  [2, 0, 1, 2]

Before: [0, 2, 0, 0]
13 0 1 1
After:  [0, 0, 0, 0]

Before: [0, 2, 2, 1]
2 2 2 1
After:  [0, 4, 2, 1]

Before: [2, 3, 3, 1]
0 2 3 1
After:  [2, 1, 3, 1]

Before: [3, 1, 2, 1]
14 2 3 2
After:  [3, 1, 1, 1]

Before: [0, 2, 2, 3]
0 2 1 2
After:  [0, 2, 0, 3]

Before: [3, 1, 2, 1]
7 1 2 0
After:  [0, 1, 2, 1]

Before: [2, 1, 1, 3]
6 2 2 0
After:  [2, 1, 1, 3]

Before: [3, 3, 2, 1]
14 2 3 0
After:  [1, 3, 2, 1]

Before: [1, 2, 0, 2]
12 0 2 2
After:  [1, 2, 0, 2]

Before: [0, 1, 0, 3]
8 0 0 3
After:  [0, 1, 0, 0]

Before: [1, 3, 1, 2]
5 3 1 1
After:  [1, 0, 1, 2]

Before: [2, 1, 1, 0]
6 2 2 1
After:  [2, 2, 1, 0]

Before: [1, 2, 2, 3]
4 0 2 2
After:  [1, 2, 0, 3]

Before: [2, 3, 2, 1]
9 3 2 3
After:  [2, 3, 2, 1]

Before: [1, 0, 2, 0]
14 2 3 3
After:  [1, 0, 2, 1]

Before: [1, 0, 1, 3]
6 2 2 2
After:  [1, 0, 2, 3]

Before: [1, 1, 0, 3]
12 0 2 1
After:  [1, 0, 0, 3]

Before: [1, 1, 2, 2]
4 0 2 3
After:  [1, 1, 2, 0]

Before: [1, 0, 2, 1]
9 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 3, 2, 1]
4 0 2 1
After:  [1, 0, 2, 1]

Before: [3, 1, 2, 0]
3 0 2 0
After:  [2, 1, 2, 0]

Before: [3, 3, 2, 0]
11 2 1 0
After:  [0, 3, 2, 0]

Before: [0, 3, 2, 2]
8 0 0 0
After:  [0, 3, 2, 2]

Before: [3, 2, 2, 0]
14 2 3 0
After:  [1, 2, 2, 0]

Before: [1, 2, 2, 3]
2 1 2 3
After:  [1, 2, 2, 4]

Before: [3, 2, 3, 0]
15 0 1 3
After:  [3, 2, 3, 2]

Before: [3, 1, 1, 2]
15 0 3 2
After:  [3, 1, 2, 2]

Before: [2, 3, 1, 3]
6 2 2 3
After:  [2, 3, 1, 2]

Before: [1, 1, 2, 3]
4 0 2 1
After:  [1, 0, 2, 3]

Before: [2, 2, 1, 0]
6 2 2 0
After:  [2, 2, 1, 0]

Before: [3, 1, 2, 1]
7 1 2 2
After:  [3, 1, 0, 1]

Before: [3, 3, 1, 2]
5 3 1 2
After:  [3, 3, 0, 2]

Before: [0, 3, 2, 1]
11 2 1 2
After:  [0, 3, 0, 1]

Before: [1, 3, 0, 2]
5 3 1 1
After:  [1, 0, 0, 2]

Before: [2, 1, 0, 3]
15 3 0 3
After:  [2, 1, 0, 2]

Before: [3, 0, 3, 1]
0 2 3 0
After:  [1, 0, 3, 1]

Before: [1, 1, 2, 3]
7 1 2 3
After:  [1, 1, 2, 0]

Before: [1, 3, 2, 3]
3 1 2 3
After:  [1, 3, 2, 2]

Before: [1, 2, 2, 1]
9 3 2 1
After:  [1, 1, 2, 1]

Before: [0, 0, 0, 3]
13 0 3 0
After:  [0, 0, 0, 3]

Before: [1, 0, 2, 3]
4 0 2 3
After:  [1, 0, 2, 0]

Before: [1, 3, 2, 2]
2 3 2 3
After:  [1, 3, 2, 4]

Before: [1, 0, 2, 1]
14 2 3 3
After:  [1, 0, 2, 1]

Before: [0, 1, 2, 1]
9 3 2 0
After:  [1, 1, 2, 1]

Before: [0, 3, 3, 2]
5 3 1 0
After:  [0, 3, 3, 2]

Before: [3, 2, 1, 0]
6 2 2 3
After:  [3, 2, 1, 2]

Before: [0, 3, 2, 3]
11 2 1 1
After:  [0, 0, 2, 3]

Before: [3, 0, 0, 1]
1 2 0 0
After:  [0, 0, 0, 1]

Before: [3, 2, 2, 3]
2 2 2 1
After:  [3, 4, 2, 3]

Before: [2, 0, 2, 3]
2 0 2 0
After:  [4, 0, 2, 3]

Before: [0, 2, 1, 3]
8 0 0 3
After:  [0, 2, 1, 0]

Before: [3, 2, 0, 0]
15 0 1 2
After:  [3, 2, 2, 0]

Before: [0, 1, 0, 2]
13 0 3 0
After:  [0, 1, 0, 2]

Before: [0, 3, 1, 3]
13 0 2 0
After:  [0, 3, 1, 3]

Before: [2, 3, 0, 2]
5 3 1 0
After:  [0, 3, 0, 2]

Before: [2, 3, 2, 1]
9 3 2 0
After:  [1, 3, 2, 1]

Before: [0, 3, 3, 1]
13 0 3 1
After:  [0, 0, 3, 1]

Before: [1, 3, 2, 0]
14 2 3 1
After:  [1, 1, 2, 0]

Before: [1, 3, 2, 1]
4 0 2 2
After:  [1, 3, 0, 1]

Before: [0, 0, 2, 1]
13 0 2 3
After:  [0, 0, 2, 0]

Before: [1, 1, 3, 1]
0 2 3 1
After:  [1, 1, 3, 1]

Before: [3, 3, 2, 2]
15 1 3 2
After:  [3, 3, 2, 2]

Before: [1, 3, 2, 2]
2 2 2 3
After:  [1, 3, 2, 4]

Before: [1, 3, 0, 3]
10 0 3 1
After:  [1, 1, 0, 3]

Before: [3, 0, 2, 1]
1 1 0 3
After:  [3, 0, 2, 0]

Before: [3, 1, 2, 1]
9 3 2 3
After:  [3, 1, 2, 1]

Before: [1, 2, 2, 3]
0 2 1 3
After:  [1, 2, 2, 0]

Before: [2, 2, 2, 1]
2 1 2 3
After:  [2, 2, 2, 4]

Before: [1, 3, 2, 1]
4 0 2 0
After:  [0, 3, 2, 1]

Before: [1, 1, 2, 1]
7 1 2 2
After:  [1, 1, 0, 1]

Before: [2, 3, 2, 2]
3 1 2 3
After:  [2, 3, 2, 2]

Before: [0, 1, 2, 1]
9 3 2 1
After:  [0, 1, 2, 1]

Before: [3, 0, 0, 3]
1 2 0 0
After:  [0, 0, 0, 3]

Before: [3, 0, 1, 1]
6 2 2 2
After:  [3, 0, 2, 1]

Before: [1, 1, 0, 2]
12 0 2 2
After:  [1, 1, 0, 2]

Before: [2, 3, 1, 3]
6 2 2 2
After:  [2, 3, 2, 3]

Before: [0, 3, 2, 3]
11 2 1 0
After:  [0, 3, 2, 3]

Before: [1, 2, 2, 3]
2 2 2 0
After:  [4, 2, 2, 3]

Before: [0, 2, 0, 2]
13 0 1 2
After:  [0, 2, 0, 2]

Before: [1, 3, 2, 3]
4 0 2 3
After:  [1, 3, 2, 0]

Before: [0, 2, 3, 3]
13 0 3 2
After:  [0, 2, 0, 3]

Before: [0, 3, 1, 2]
5 3 1 3
After:  [0, 3, 1, 0]

Before: [1, 0, 2, 1]
14 2 3 0
After:  [1, 0, 2, 1]

Before: [2, 2, 2, 0]
0 2 1 1
After:  [2, 0, 2, 0]

Before: [2, 3, 1, 2]
5 3 1 3
After:  [2, 3, 1, 0]

Before: [0, 2, 0, 1]
13 0 1 0
After:  [0, 2, 0, 1]

Before: [2, 2, 3, 3]
15 3 1 2
After:  [2, 2, 2, 3]

Before: [0, 1, 2, 3]
2 2 2 0
After:  [4, 1, 2, 3]

Before: [3, 1, 2, 0]
7 1 2 0
After:  [0, 1, 2, 0]

Before: [1, 2, 0, 2]
12 0 2 0
After:  [0, 2, 0, 2]

Before: [0, 0, 0, 0]
8 0 0 3
After:  [0, 0, 0, 0]

Before: [0, 2, 3, 2]
8 0 0 3
After:  [0, 2, 3, 0]

Before: [0, 1, 2, 2]
2 3 2 0
After:  [4, 1, 2, 2]

Before: [1, 3, 2, 0]
14 2 3 0
After:  [1, 3, 2, 0]

Before: [1, 2, 2, 3]
0 2 1 2
After:  [1, 2, 0, 3]

Before: [0, 2, 3, 3]
13 0 2 3
After:  [0, 2, 3, 0]

Before: [3, 3, 2, 0]
11 2 1 2
After:  [3, 3, 0, 0]

Before: [0, 3, 3, 2]
8 0 0 3
After:  [0, 3, 3, 0]

Before: [2, 1, 1, 0]
6 2 2 3
After:  [2, 1, 1, 2]

Before: [3, 3, 1, 1]
6 2 2 0
After:  [2, 3, 1, 1]

Before: [1, 1, 2, 3]
7 1 2 1
After:  [1, 0, 2, 3]

Before: [0, 1, 0, 1]
13 0 1 2
After:  [0, 1, 0, 1]

Before: [0, 1, 3, 1]
8 0 0 3
After:  [0, 1, 3, 0]

Before: [3, 3, 2, 0]
11 2 1 1
After:  [3, 0, 2, 0]

Before: [0, 1, 0, 0]
8 0 0 0
After:  [0, 1, 0, 0]

Before: [0, 2, 3, 0]
8 0 0 3
After:  [0, 2, 3, 0]

Before: [3, 0, 3, 2]
1 1 0 0
After:  [0, 0, 3, 2]

Before: [1, 0, 3, 1]
0 2 3 3
After:  [1, 0, 3, 1]

Before: [2, 3, 2, 3]
11 2 1 3
After:  [2, 3, 2, 0]

Before: [1, 1, 1, 1]
6 2 2 2
After:  [1, 1, 2, 1]

Before: [2, 3, 2, 2]
5 3 1 3
After:  [2, 3, 2, 0]

Before: [2, 3, 2, 1]
9 3 2 2
After:  [2, 3, 1, 1]

Before: [0, 2, 3, 1]
13 0 1 0
After:  [0, 2, 3, 1]

Before: [1, 0, 1, 3]
10 2 3 2
After:  [1, 0, 1, 3]

Before: [0, 3, 1, 2]
5 3 1 1
After:  [0, 0, 1, 2]

Before: [3, 0, 0, 3]
1 1 0 2
After:  [3, 0, 0, 3]

Before: [2, 3, 2, 1]
11 2 1 3
After:  [2, 3, 2, 0]

Before: [3, 2, 2, 1]
9 3 2 0
After:  [1, 2, 2, 1]

Before: [2, 2, 1, 2]
6 2 2 1
After:  [2, 2, 1, 2]

Before: [2, 3, 2, 3]
11 2 1 0
After:  [0, 3, 2, 3]

Before: [1, 3, 2, 0]
4 0 2 0
After:  [0, 3, 2, 0]

Before: [3, 1, 2, 2]
7 1 2 0
After:  [0, 1, 2, 2]

Before: [3, 1, 2, 3]
7 1 2 0
After:  [0, 1, 2, 3]

Before: [2, 3, 2, 3]
10 0 3 0
After:  [2, 3, 2, 3]

Before: [3, 2, 2, 3]
0 2 1 1
After:  [3, 0, 2, 3]

Before: [2, 0, 2, 0]
1 1 0 1
After:  [2, 0, 2, 0]

Before: [0, 3, 0, 2]
5 3 1 2
After:  [0, 3, 0, 2]

Before: [2, 2, 2, 1]
9 3 2 2
After:  [2, 2, 1, 1]

Before: [1, 1, 0, 1]
12 0 2 0
After:  [0, 1, 0, 1]

Before: [1, 0, 2, 1]
9 3 2 3
After:  [1, 0, 2, 1]

Before: [3, 2, 2, 3]
0 2 1 2
After:  [3, 2, 0, 3]

Before: [3, 0, 2, 2]
2 3 2 3
After:  [3, 0, 2, 4]

Before: [1, 0, 2, 2]
4 0 2 0
After:  [0, 0, 2, 2]

Before: [3, 3, 2, 2]
11 2 1 1
After:  [3, 0, 2, 2]

Before: [0, 1, 3, 1]
0 2 3 3
After:  [0, 1, 3, 1]

Before: [0, 0, 1, 0]
8 0 0 1
After:  [0, 0, 1, 0]

Before: [2, 0, 2, 1]
9 3 2 0
After:  [1, 0, 2, 1]

Before: [3, 0, 2, 2]
1 1 0 2
After:  [3, 0, 0, 2]

Before: [3, 3, 0, 1]
1 2 0 2
After:  [3, 3, 0, 1]

Before: [3, 2, 3, 3]
10 1 3 3
After:  [3, 2, 3, 2]

Before: [2, 3, 3, 1]
0 2 3 2
After:  [2, 3, 1, 1]

Before: [3, 1, 2, 2]
7 1 2 3
After:  [3, 1, 2, 0]

Before: [0, 3, 0, 3]
8 0 0 3
After:  [0, 3, 0, 0]

Before: [3, 0, 2, 2]
2 2 2 0
After:  [4, 0, 2, 2]

Before: [2, 3, 3, 3]
15 3 0 3
After:  [2, 3, 3, 2]

Before: [0, 2, 0, 1]
13 0 3 2
After:  [0, 2, 0, 1]

Before: [1, 2, 0, 3]
15 3 1 0
After:  [2, 2, 0, 3]

Before: [2, 2, 2, 2]
0 2 1 0
After:  [0, 2, 2, 2]

Before: [2, 0, 3, 1]
1 1 0 0
After:  [0, 0, 3, 1]

Before: [0, 0, 2, 1]
14 2 3 1
After:  [0, 1, 2, 1]

Before: [2, 2, 2, 1]
2 0 2 2
After:  [2, 2, 4, 1]

Before: [0, 3, 2, 1]
9 3 2 2
After:  [0, 3, 1, 1]

Before: [0, 3, 2, 2]
5 3 1 1
After:  [0, 0, 2, 2]

Before: [1, 2, 2, 2]
4 0 2 2
After:  [1, 2, 0, 2]

Before: [1, 1, 1, 3]
10 2 3 3
After:  [1, 1, 1, 1]

Before: [0, 2, 1, 1]
13 0 2 0
After:  [0, 2, 1, 1]

Before: [0, 3, 2, 2]
11 2 1 0
After:  [0, 3, 2, 2]

Before: [0, 2, 1, 2]
8 0 0 3
After:  [0, 2, 1, 0]

Before: [0, 3, 2, 2]
15 1 3 1
After:  [0, 2, 2, 2]

Before: [3, 0, 2, 0]
2 2 2 3
After:  [3, 0, 2, 4]

Before: [2, 2, 3, 3]
10 0 3 3
After:  [2, 2, 3, 2]

Before: [0, 2, 0, 3]
8 0 0 2
After:  [0, 2, 0, 3]

Before: [2, 2, 1, 3]
6 2 2 3
After:  [2, 2, 1, 2]

Before: [1, 2, 2, 0]
14 2 3 1
After:  [1, 1, 2, 0]

Before: [0, 3, 2, 1]
11 2 1 0
After:  [0, 3, 2, 1]

Before: [3, 3, 2, 1]
11 2 1 2
After:  [3, 3, 0, 1]

Before: [2, 3, 1, 3]
10 0 3 2
After:  [2, 3, 2, 3]

Before: [3, 1, 1, 1]
6 2 2 2
After:  [3, 1, 2, 1]

Before: [3, 2, 2, 0]
0 2 1 2
After:  [3, 2, 0, 0]

Before: [1, 3, 0, 2]
12 0 2 3
After:  [1, 3, 0, 0]

Before: [2, 3, 0, 2]
5 3 1 3
After:  [2, 3, 0, 0]

Before: [0, 1, 1, 0]
13 0 2 0
After:  [0, 1, 1, 0]

Before: [3, 3, 2, 1]
11 2 1 3
After:  [3, 3, 2, 0]

Before: [0, 1, 1, 3]
13 0 2 0
After:  [0, 1, 1, 3]

Before: [3, 3, 2, 3]
11 2 1 0
After:  [0, 3, 2, 3]

Before: [1, 1, 2, 1]
9 3 2 1
After:  [1, 1, 2, 1]

Before: [1, 1, 2, 1]
7 1 2 1
After:  [1, 0, 2, 1]

Before: [3, 2, 2, 3]
10 1 3 3
After:  [3, 2, 2, 2]

Before: [1, 2, 2, 3]
4 0 2 3
After:  [1, 2, 2, 0]

Before: [1, 3, 2, 3]
11 2 1 3
After:  [1, 3, 2, 0]

Before: [0, 0, 2, 1]
13 0 3 1
After:  [0, 0, 2, 1]

Before: [0, 1, 2, 0]
7 1 2 2
After:  [0, 1, 0, 0]

Before: [0, 3, 1, 3]
10 2 3 0
After:  [1, 3, 1, 3]

Before: [1, 1, 2, 2]
4 0 2 2
After:  [1, 1, 0, 2]

Before: [0, 1, 2, 3]
3 3 2 0
After:  [2, 1, 2, 3]

Before: [2, 0, 1, 2]
6 2 2 0
After:  [2, 0, 1, 2]

Before: [3, 0, 1, 2]
1 1 0 0
After:  [0, 0, 1, 2]

Before: [1, 2, 1, 3]
6 2 2 0
After:  [2, 2, 1, 3]

Before: [2, 3, 2, 0]
11 2 1 1
After:  [2, 0, 2, 0]

Before: [2, 3, 1, 1]
6 2 2 1
After:  [2, 2, 1, 1]

Before: [1, 0, 2, 1]
9 3 2 2
After:  [1, 0, 1, 1]

Before: [2, 3, 1, 3]
10 2 3 0
After:  [1, 3, 1, 3]

Before: [1, 2, 2, 1]
9 3 2 2
After:  [1, 2, 1, 1]

Before: [1, 3, 0, 1]
12 0 2 1
After:  [1, 0, 0, 1]

Before: [1, 2, 1, 3]
10 0 3 1
After:  [1, 1, 1, 3]

Before: [3, 0, 1, 3]
6 2 2 0
After:  [2, 0, 1, 3]

Before: [2, 3, 1, 3]
10 2 3 2
After:  [2, 3, 1, 3]

Before: [0, 1, 2, 1]
9 3 2 2
After:  [0, 1, 1, 1]

Before: [0, 3, 1, 2]
5 3 1 2
After:  [0, 3, 0, 2]

Before: [0, 2, 2, 1]
9 3 2 3
After:  [0, 2, 2, 1]

Before: [1, 3, 2, 2]
5 3 1 0
After:  [0, 3, 2, 2]

Before: [0, 1, 2, 0]
2 2 2 3
After:  [0, 1, 2, 4]

Before: [0, 3, 2, 3]
11 2 1 2
After:  [0, 3, 0, 3]

Before: [1, 3, 2, 0]
2 2 2 0
After:  [4, 3, 2, 0]

Before: [0, 1, 2, 3]
7 1 2 0
After:  [0, 1, 2, 3]

Before: [0, 1, 2, 1]
14 2 3 3
After:  [0, 1, 2, 1]

Before: [3, 3, 2, 0]
11 2 1 3
After:  [3, 3, 2, 0]

Before: [1, 3, 2, 1]
11 2 1 1
After:  [1, 0, 2, 1]

Before: [3, 3, 3, 2]
15 0 3 0
After:  [2, 3, 3, 2]

Before: [3, 3, 2, 2]
5 3 1 3
After:  [3, 3, 2, 0]

Before: [1, 0, 0, 2]
12 0 2 1
After:  [1, 0, 0, 2]

Before: [1, 0, 0, 3]
12 0 2 1
After:  [1, 0, 0, 3]

Before: [1, 3, 0, 2]
5 3 1 3
After:  [1, 3, 0, 0]

Before: [1, 1, 2, 3]
4 0 2 0
After:  [0, 1, 2, 3]

Before: [1, 0, 2, 0]
14 2 3 0
After:  [1, 0, 2, 0]

Before: [3, 3, 0, 3]
1 2 0 0
After:  [0, 3, 0, 3]

Before: [3, 3, 2, 1]
3 0 2 1
After:  [3, 2, 2, 1]

Before: [1, 3, 2, 0]
4 0 2 2
After:  [1, 3, 0, 0]

Before: [3, 2, 0, 1]
15 0 1 1
After:  [3, 2, 0, 1]

Before: [0, 3, 2, 3]
2 2 2 0
After:  [4, 3, 2, 3]

Before: [1, 0, 0, 0]
12 0 2 1
After:  [1, 0, 0, 0]

Before: [0, 0, 0, 1]
8 0 0 3
After:  [0, 0, 0, 0]

Before: [1, 3, 2, 3]
4 0 2 2
After:  [1, 3, 0, 3]

Before: [1, 3, 0, 0]
12 0 2 2
After:  [1, 3, 0, 0]

Before: [2, 2, 0, 3]
10 0 3 1
After:  [2, 2, 0, 3]

Before: [3, 0, 3, 3]
1 1 0 2
After:  [3, 0, 0, 3]

Before: [3, 3, 2, 2]
11 2 1 0
After:  [0, 3, 2, 2]

Before: [1, 2, 1, 3]
10 2 3 0
After:  [1, 2, 1, 3]

Before: [3, 3, 2, 3]
11 2 1 3
After:  [3, 3, 2, 0]

Before: [3, 2, 2, 0]
0 2 1 3
After:  [3, 2, 2, 0]

Before: [0, 2, 3, 1]
8 0 0 0
After:  [0, 2, 3, 1]

Before: [3, 0, 1, 2]
1 1 0 1
After:  [3, 0, 1, 2]

Before: [1, 1, 3, 1]
0 2 3 2
After:  [1, 1, 1, 1]

Before: [1, 2, 0, 0]
12 0 2 2
After:  [1, 2, 0, 0]

Before: [3, 0, 0, 0]
1 2 0 2
After:  [3, 0, 0, 0]

Before: [2, 1, 2, 3]
3 3 2 3
After:  [2, 1, 2, 2]

Before: [0, 2, 2, 0]
14 2 3 1
After:  [0, 1, 2, 0]

Before: [2, 3, 1, 2]
5 3 1 2
After:  [2, 3, 0, 2]

Before: [2, 2, 0, 3]
15 3 0 0
After:  [2, 2, 0, 3]

Before: [0, 2, 3, 2]
8 0 0 0
After:  [0, 2, 3, 2]

Before: [1, 3, 2, 1]
11 2 1 3
After:  [1, 3, 2, 0]

Before: [2, 1, 2, 1]
9 3 2 0
After:  [1, 1, 2, 1]

Before: [2, 2, 1, 3]
6 2 2 2
After:  [2, 2, 2, 3]

Before: [2, 3, 2, 1]
14 2 3 0
After:  [1, 3, 2, 1]

Before: [1, 3, 1, 3]
10 2 3 0
After:  [1, 3, 1, 3]

Before: [3, 3, 0, 2]
5 3 1 2
After:  [3, 3, 0, 2]

Before: [0, 3, 2, 3]
13 0 2 1
After:  [0, 0, 2, 3]

Before: [1, 0, 1, 1]
6 2 2 2
After:  [1, 0, 2, 1]

Before: [3, 3, 2, 2]
5 3 1 0
After:  [0, 3, 2, 2]

Before: [2, 1, 2, 1]
7 1 2 0
After:  [0, 1, 2, 1]

Before: [1, 1, 0, 0]
12 0 2 1
After:  [1, 0, 0, 0]

Before: [3, 3, 1, 0]
6 2 2 1
After:  [3, 2, 1, 0]

Before: [0, 1, 2, 0]
13 0 2 0
After:  [0, 1, 2, 0]

Before: [3, 3, 2, 0]
3 0 2 2
After:  [3, 3, 2, 0]

Before: [0, 1, 2, 1]
14 2 3 0
After:  [1, 1, 2, 1]

Before: [2, 3, 3, 0]
15 1 0 1
After:  [2, 2, 3, 0]

Before: [3, 2, 2, 2]
2 3 2 1
After:  [3, 4, 2, 2]

Before: [2, 2, 2, 3]
0 2 1 3
After:  [2, 2, 2, 0]

Before: [3, 0, 2, 2]
1 1 0 1
After:  [3, 0, 2, 2]

Before: [1, 2, 2, 0]
4 0 2 1
After:  [1, 0, 2, 0]

Before: [3, 3, 2, 0]
2 2 2 3
After:  [3, 3, 2, 4]

Before: [3, 2, 1, 3]
15 0 1 1
After:  [3, 2, 1, 3]

Before: [1, 3, 0, 0]
12 0 2 1
After:  [1, 0, 0, 0]

Before: [3, 3, 2, 3]
11 2 1 1
After:  [3, 0, 2, 3]

Before: [2, 0, 1, 1]
6 2 2 1
After:  [2, 2, 1, 1]

Before: [2, 1, 2, 1]
2 0 2 2
After:  [2, 1, 4, 1]

Before: [1, 0, 2, 3]
4 0 2 0
After:  [0, 0, 2, 3]

Before: [0, 3, 2, 1]
14 2 3 0
After:  [1, 3, 2, 1]

Before: [3, 2, 1, 3]
15 3 1 2
After:  [3, 2, 2, 3]

Before: [2, 0, 3, 3]
10 0 3 2
After:  [2, 0, 2, 3]

Before: [3, 0, 0, 2]
1 1 0 0
After:  [0, 0, 0, 2]

Before: [1, 3, 0, 3]
12 0 2 3
After:  [1, 3, 0, 0]

Before: [0, 1, 1, 2]
8 0 0 0
After:  [0, 1, 1, 2]

Before: [0, 3, 1, 1]
6 2 2 2
After:  [0, 3, 2, 1]

Before: [3, 3, 2, 2]
2 2 2 2
After:  [3, 3, 4, 2]

Before: [0, 3, 2, 3]
13 0 3 1
After:  [0, 0, 2, 3]

Before: [0, 1, 2, 2]
7 1 2 3
After:  [0, 1, 2, 0]

Before: [2, 2, 2, 1]
0 2 1 3
After:  [2, 2, 2, 0]

Before: [2, 3, 0, 2]
5 3 1 1
After:  [2, 0, 0, 2]

Before: [3, 2, 3, 0]
15 0 1 1
After:  [3, 2, 3, 0]

Before: [0, 3, 2, 2]
11 2 1 1
After:  [0, 0, 2, 2]

Before: [1, 1, 1, 3]
10 2 3 2
After:  [1, 1, 1, 3]

Before: [1, 0, 3, 1]
0 2 3 2
After:  [1, 0, 1, 1]

Before: [0, 3, 3, 1]
13 0 2 3
After:  [0, 3, 3, 0]

Before: [3, 2, 2, 1]
14 2 3 3
After:  [3, 2, 2, 1]

Before: [0, 0, 2, 3]
8 0 0 1
After:  [0, 0, 2, 3]

Before: [0, 3, 3, 3]
13 0 3 3
After:  [0, 3, 3, 0]

Before: [1, 3, 2, 3]
11 2 1 0
After:  [0, 3, 2, 3]

Before: [3, 0, 0, 1]
1 1 0 3
After:  [3, 0, 0, 0]

Before: [0, 3, 1, 1]
8 0 0 3
After:  [0, 3, 1, 0]

Before: [0, 0, 2, 3]
13 0 2 2
After:  [0, 0, 0, 3]

Before: [3, 1, 3, 1]
0 2 3 0
After:  [1, 1, 3, 1]

Before: [3, 2, 2, 2]
3 0 2 2
After:  [3, 2, 2, 2]

Before: [1, 3, 0, 3]
12 0 2 2
After:  [1, 3, 0, 3]

Before: [1, 3, 2, 1]
14 2 3 0
After:  [1, 3, 2, 1]

Before: [2, 2, 2, 2]
2 2 2 3
After:  [2, 2, 2, 4]

Before: [2, 1, 1, 2]
6 2 2 2
After:  [2, 1, 2, 2]

Before: [2, 0, 3, 3]
1 1 0 1
After:  [2, 0, 3, 3]

Before: [3, 2, 2, 3]
15 0 1 2
After:  [3, 2, 2, 3]



4 0 2 0
13 2 0 2
2 2 3 2
4 3 2 3
3 3 2 2
13 2 1 2
6 2 1 1
10 1 2 3
4 2 3 0
13 1 0 1
2 1 1 1
13 3 0 2
2 2 1 2
12 1 0 1
13 1 2 1
6 1 3 3
10 3 1 1
4 0 1 2
4 2 2 3
5 0 3 3
13 3 1 3
6 3 1 1
4 2 1 2
4 0 3 3
9 3 2 2
13 2 1 2
13 2 1 2
6 1 2 1
10 1 3 0
4 0 0 1
13 0 0 2
2 2 2 2
9 3 2 1
13 1 2 1
6 1 0 0
10 0 3 3
4 1 1 0
4 2 0 1
10 0 2 0
13 0 3 0
6 3 0 3
13 3 0 0
2 0 2 0
13 3 0 2
2 2 3 2
8 1 2 0
13 0 1 0
13 0 2 0
6 0 3 3
10 3 2 1
13 2 0 2
2 2 2 2
13 2 0 0
2 0 1 0
13 1 0 3
2 3 2 3
10 0 2 2
13 2 3 2
6 2 1 1
10 1 2 2
4 0 3 3
4 2 1 0
13 2 0 1
2 1 3 1
1 0 3 0
13 0 1 0
6 0 2 2
10 2 1 1
4 3 0 2
4 1 2 0
4 2 0 3
12 0 3 0
13 0 3 0
6 0 1 1
10 1 1 2
4 1 1 1
4 3 3 0
12 1 3 0
13 0 1 0
6 0 2 2
10 2 3 3
4 3 0 1
4 0 3 2
4 2 2 0
3 1 2 1
13 1 1 1
6 1 3 3
10 3 2 2
4 2 0 3
4 0 1 1
5 0 3 1
13 1 1 1
6 2 1 2
10 2 3 3
4 3 1 1
13 3 0 2
2 2 0 2
7 0 1 2
13 2 2 2
6 2 3 3
4 3 1 2
0 0 2 2
13 2 3 2
6 3 2 3
10 3 1 0
4 0 2 1
4 3 0 3
4 0 0 2
3 3 2 1
13 1 1 1
13 1 1 1
6 1 0 0
10 0 1 2
4 0 1 1
4 1 0 3
13 3 0 0
2 0 2 0
2 3 1 1
13 1 3 1
13 1 2 1
6 1 2 2
10 2 0 3
4 3 0 2
13 0 0 1
2 1 2 1
4 0 1 0
8 1 2 1
13 1 2 1
6 1 3 3
10 3 2 2
4 2 3 0
4 3 1 1
4 0 1 3
7 0 1 3
13 3 2 3
6 3 2 2
10 2 0 3
4 3 3 0
4 3 0 2
3 1 2 1
13 1 3 1
6 3 1 3
10 3 3 0
4 1 2 3
4 3 3 1
13 3 0 2
2 2 2 2
7 2 1 2
13 2 1 2
13 2 1 2
6 0 2 0
10 0 1 3
4 0 1 1
4 1 3 0
4 1 1 2
2 0 1 0
13 0 1 0
6 0 3 3
10 3 1 0
4 2 2 2
4 3 1 1
4 0 1 3
9 3 2 2
13 2 1 2
6 0 2 0
10 0 0 1
4 2 2 0
13 2 0 3
2 3 1 3
4 2 1 2
14 0 3 3
13 3 3 3
6 3 1 1
4 2 0 3
4 3 3 0
15 0 3 0
13 0 1 0
6 1 0 1
10 1 3 2
13 3 0 0
2 0 2 0
4 1 2 1
1 0 3 0
13 0 2 0
6 2 0 2
10 2 3 0
4 0 3 3
4 3 3 1
13 2 0 2
2 2 2 2
9 3 2 3
13 3 1 3
13 3 1 3
6 3 0 0
10 0 0 3
4 2 0 1
4 0 1 2
4 3 1 0
0 2 0 0
13 0 1 0
13 0 1 0
6 3 0 3
10 3 3 1
4 2 2 3
13 2 0 0
2 0 3 0
0 2 0 2
13 2 1 2
13 2 3 2
6 2 1 1
10 1 2 3
4 0 2 2
4 2 0 1
3 0 2 2
13 2 3 2
6 2 3 3
4 0 0 1
4 1 2 0
4 0 3 2
6 0 0 0
13 0 2 0
13 0 1 0
6 0 3 3
4 1 2 0
4 3 0 1
4 2 0 2
10 0 2 0
13 0 3 0
6 3 0 3
10 3 3 0
4 2 2 1
4 2 1 3
4 0 2 2
11 2 3 3
13 3 1 3
6 0 3 0
10 0 0 1
4 2 2 2
4 0 1 3
4 1 1 0
9 3 2 3
13 3 2 3
6 3 1 1
10 1 1 3
13 3 0 1
2 1 2 1
4 0 3 2
13 0 2 1
13 1 1 1
13 1 1 1
6 3 1 3
10 3 0 1
4 3 1 0
4 3 3 2
4 0 1 3
11 3 2 2
13 2 3 2
6 1 2 1
10 1 3 0
13 3 0 2
2 2 2 2
4 0 1 1
4 3 1 3
13 3 1 3
6 0 3 0
10 0 3 1
4 0 0 0
4 3 2 2
4 0 1 3
11 3 2 0
13 0 3 0
6 0 1 1
10 1 0 2
13 3 0 3
2 3 2 3
4 2 3 0
4 3 0 1
1 0 3 3
13 3 1 3
6 3 2 2
10 2 0 1
4 3 2 2
13 0 0 3
2 3 2 3
4 3 0 0
15 0 3 0
13 0 1 0
13 0 2 0
6 0 1 1
4 2 2 2
4 0 0 3
4 3 0 0
9 3 2 2
13 2 3 2
13 2 2 2
6 2 1 1
10 1 3 2
4 2 2 3
13 3 0 1
2 1 1 1
4 1 0 0
12 0 3 1
13 1 1 1
13 1 3 1
6 1 2 2
10 2 3 1
4 3 0 0
4 0 1 3
4 2 2 2
9 3 2 3
13 3 3 3
6 3 1 1
10 1 3 0
13 1 0 1
2 1 3 1
4 2 3 3
4 0 3 2
11 2 3 3
13 3 2 3
6 0 3 0
10 0 1 3
4 2 0 1
4 2 3 2
4 1 1 0
6 0 0 2
13 2 2 2
13 2 3 2
6 2 3 3
10 3 1 0
4 1 3 3
4 3 0 2
4 3 1 1
4 2 1 2
13 2 2 2
6 2 0 0
10 0 2 3
4 0 2 0
4 3 1 2
4 2 0 1
8 1 2 2
13 2 2 2
6 2 3 3
10 3 1 1
13 0 0 0
2 0 2 0
13 0 0 3
2 3 1 3
4 3 3 2
14 0 3 3
13 3 1 3
13 3 2 3
6 1 3 1
10 1 1 3
4 0 1 0
4 1 3 1
4 0 1 2
13 1 2 0
13 0 3 0
6 0 3 3
10 3 2 2
13 2 0 0
2 0 2 0
4 2 3 3
5 0 3 3
13 3 1 3
6 2 3 2
10 2 2 1
4 1 2 3
4 3 3 0
4 0 1 2
13 3 2 2
13 2 3 2
6 1 2 1
10 1 1 3
13 3 0 0
2 0 1 0
4 2 3 2
4 2 0 1
10 0 2 2
13 2 1 2
13 2 1 2
6 2 3 3
10 3 0 1
4 0 3 0
4 0 0 3
4 1 3 2
4 3 2 3
13 3 3 3
6 3 1 1
10 1 2 2
4 2 0 3
4 2 0 0
4 2 1 1
5 0 3 1
13 1 2 1
6 1 2 2
10 2 3 1
4 1 2 3
4 2 1 2
14 0 3 0
13 0 1 0
6 0 1 1
10 1 3 3
4 3 0 2
13 0 0 0
2 0 2 0
13 3 0 1
2 1 1 1
0 0 2 1
13 1 3 1
6 3 1 3
10 3 2 0
4 0 1 1
4 3 0 3
4 0 3 2
4 2 3 1
13 1 2 1
6 0 1 0
10 0 3 2
4 3 1 1
4 1 3 0
4 2 1 3
12 0 3 1
13 1 1 1
6 2 1 2
4 3 2 1
4 2 0 0
4 0 0 3
1 0 3 1
13 1 3 1
6 2 1 2
10 2 1 1
4 3 3 0
4 0 0 2
0 2 0 3
13 3 2 3
6 3 1 1
10 1 0 0
4 0 0 3
4 2 0 1
13 0 0 2
2 2 3 2
8 1 2 3
13 3 3 3
6 0 3 0
10 0 0 2
4 1 1 1
4 2 3 0
4 2 0 3
5 0 3 1
13 1 1 1
13 1 3 1
6 2 1 2
10 2 1 0
4 1 1 1
4 0 1 3
4 2 0 2
9 3 2 3
13 3 1 3
6 0 3 0
10 0 3 1
13 2 0 0
2 0 2 0
4 3 1 3
15 3 0 0
13 0 3 0
13 0 1 0
6 1 0 1
10 1 1 0
13 1 0 1
2 1 1 1
13 3 0 3
2 3 2 3
1 2 3 3
13 3 2 3
6 0 3 0
10 0 1 2
4 2 1 0
4 0 2 1
4 2 1 3
5 0 3 0
13 0 3 0
6 0 2 2
10 2 0 3
13 0 0 0
2 0 2 0
4 3 2 2
4 1 3 1
13 1 2 2
13 2 2 2
6 2 3 3
10 3 0 1
13 0 0 3
2 3 3 3
4 3 1 0
4 0 2 2
0 2 0 3
13 3 1 3
6 1 3 1
10 1 0 0
4 3 2 2
4 0 3 3
4 2 0 1
11 3 2 1
13 1 3 1
6 0 1 0
4 1 3 1
4 1 1 3
13 3 2 3
13 3 3 3
13 3 2 3
6 0 3 0
10 0 2 1
4 0 0 3
4 0 2 0
11 3 2 2
13 2 1 2
6 2 1 1
4 2 2 0
4 3 1 2
4 2 2 3
5 0 3 3
13 3 2 3
13 3 3 3
6 3 1 1
10 1 2 0
4 0 2 3
13 0 0 1
2 1 2 1
8 1 2 1
13 1 3 1
6 0 1 0
4 0 0 1
4 2 3 2
1 2 3 1
13 1 1 1
13 1 3 1
6 1 0 0
10 0 2 1
13 1 0 0
2 0 0 0
4 0 1 2
13 0 0 3
2 3 2 3
11 2 3 2
13 2 2 2
13 2 1 2
6 2 1 1
13 1 0 0
2 0 2 0
4 0 3 3
4 2 2 2
1 2 3 0
13 0 3 0
6 0 1 1
10 1 3 0
4 2 0 1
4 3 1 2
1 1 3 2
13 2 1 2
6 2 0 0
10 0 3 2
4 2 2 0
4 1 0 1
13 3 0 3
2 3 2 3
12 1 0 0
13 0 1 0
6 2 0 2
4 2 1 0
5 0 3 0
13 0 2 0
6 0 2 2
10 2 3 1
13 2 0 0
2 0 3 0
4 0 2 3
4 2 1 2
8 2 0 3
13 3 1 3
6 1 3 1
10 1 1 2
4 2 2 0
13 2 0 1
2 1 3 1
4 2 3 3
7 0 1 0
13 0 2 0
6 2 0 2
10 2 2 1
4 0 1 3
4 0 2 0
4 2 3 2
9 3 2 3
13 3 2 3
6 1 3 1
4 1 0 0
4 3 2 3
10 0 2 2
13 2 1 2
6 1 2 1
10 1 0 2
4 3 1 1
4 2 2 0
4 0 1 3
7 0 1 0
13 0 2 0
13 0 3 0
6 2 0 2
10 2 3 3
4 2 2 0
13 3 0 1
2 1 1 1
4 0 0 2
13 1 2 2
13 2 2 2
13 2 1 2
6 2 3 3
4 0 3 2
4 3 2 0
0 2 0 1
13 1 1 1
6 3 1 3
10 3 2 1
13 0 0 2
2 2 3 2
4 1 2 3
4 2 1 0
0 0 2 2
13 2 1 2
13 2 2 2
6 2 1 1
10 1 2 2
4 3 0 1
13 2 0 3
2 3 2 3
7 0 1 1
13 1 1 1
13 1 1 1
6 2 1 2
10 2 3 3
4 3 3 1
4 1 1 0
4 2 0 2
7 2 1 2
13 2 3 2
6 3 2 3
4 2 2 1
4 3 1 0
4 0 0 2
3 0 2 1
13 1 3 1
6 1 3 3
10 3 1 0
4 2 0 1
4 2 3 2
13 3 0 3
2 3 0 3
1 1 3 1
13 1 2 1
6 0 1 0
10 0 0 1
4 1 1 2
13 3 0 3
2 3 3 3
4 2 3 0
15 3 0 0
13 0 1 0
13 0 3 0
6 0 1 1
4 1 0 0
4 1 2 3
13 0 0 2
2 2 2 2
10 0 2 3
13 3 3 3
13 3 3 3
6 3 1 1
4 3 0 0
13 1 0 3
2 3 2 3
7 2 0 0
13 0 2 0
13 0 3 0
6 0 1 1
13 2 0 0
2 0 0 0
13 2 0 3
2 3 1 3
4 3 0 2
13 3 2 0
13 0 3 0
6 1 0 1
10 1 1 0
4 0 0 2
4 1 3 1
13 1 2 2
13 2 2 2
6 2 0 0
4 1 1 2
4 3 0 1
4 2 0 3
15 1 3 1
13 1 1 1
13 1 3 1
6 1 0 0
13 2 0 2
2 2 2 2
4 0 3 3
4 0 3 1
9 3 2 2
13 2 3 2
6 2 0 0
4 2 0 2
4 2 0 1
9 3 2 3
13 3 3 3
13 3 3 3
6 3 0 0
10 0 0 1
4 2 1 0
4 1 3 2
4 2 1 3
5 0 3 2
13 2 2 2
13 2 1 2
6 2 1 1
4 0 0 0
13 0 0 2
2 2 0 2
13 1 0 3
2 3 1 3
6 3 3 0
13 0 2 0
13 0 1 0
6 0 1 1
4 1 2 0
4 2 1 3
6 0 0 2
13 2 1 2
13 2 1 2
6 2 1 1
10 1 1 2
4 1 2 3
4 0 2 1
4 2 0 0
14 0 3 1
13 1 2 1
13 1 2 1
6 2 1 2
10 2 2 0
4 1 2 2
4 3 2 3
4 3 0 1
3 1 2 2
13 2 1 2
13 2 2 2
6 2 0 0
10 0 1 3
4 3 3 0
4 2 1 2
4 2 3 1
7 2 0 2
13 2 3 2
6 3 2 3
10 3 3 1
4 2 2 0
4 2 3 3
4 3 2 2
5 0 3 2
13 2 1 2
13 2 2 2
6 1 2 1
4 1 2 0
13 3 0 3
2 3 0 3
4 3 2 2
11 3 2 0
13 0 3 0
13 0 2 0
6 0 1 1
4 0 0 2
4 1 1 0
4 3 2 3
3 3 2 3
13 3 2 3
6 1 3 1
4 2 3 3
4 2 0 0
11 2 3 0
13 0 2 0
6 0 1 1
10 1 3 3
4 1 1 0
13 3 0 1
2 1 0 1
2 0 1 0
13 0 3 0
6 0 3 3
10 3 2 2
13 1 0 0
2 0 2 0
4 3 3 1
4 1 0 3
14 0 3 0
13 0 2 0
6 2 0 2
4 1 3 0
4 2 0 3
4 2 2 1
12 0 3 3
13 3 3 3
6 2 3 2
10 2 2 1
4 3 3 2
13 0 0 3
2 3 1 3
6 3 3 0
13 0 1 0
6 0 1 1
10 1 0 3
4 1 0 0
4 0 2 1
4 2 1 2
10 0 2 1
13 1 2 1
6 3 1 3
10 3 3 0
4 0 2 1
4 3 3 2
4 0 1 3
11 3 2 3
13 3 3 3
13 3 2 3
6 3 0 0
4 0 0 2
4 3 3 1
13 1 0 3
2 3 2 3
11 2 3 2
13 2 3 2
6 0 2 0
10 0 3 3
4 0 0 2
4 1 0 1
4 1 0 0
13 1 2 2
13 2 2 2
6 3 2 3
10 3 2 2
4 0 0 1
4 0 2 3
2 0 1 1
13 1 3 1
13 1 1 1
6 2 1 2
10 2 3 0
4 3 0 1
4 1 1 3
4 0 3 2
2 3 1 3
13 3 2 3
13 3 1 3
6 0 3 0
10 0 1 1
4 2 3 2
4 0 3 3
4 1 1 0
9 3 2 2
13 2 3 2
6 1 2 1
4 2 3 3
4 2 2 0
13 2 0 2
2 2 1 2
5 0 3 0
13 0 3 0
6 0 1 1
4 0 2 2
4 3 0 0
11 2 3 3
13 3 2 3
13 3 3 3
6 1 3 1
10 1 0 0
4 0 3 3
13 1 0 1
2 1 3 1
4 2 3 2
7 2 1 3
13 3 2 3
6 0 3 0'''
