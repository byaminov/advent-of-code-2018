import unittest
from aoc.day6 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual(17, solve1('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9'''))
        self.assertEqual(4475, solve1(text))

    def test_solve2(self):
        self.assertEqual(16, solve2('''1, 1
1, 6
8, 3
3, 4
5, 5
8, 9''', max_distance=32))
        self.assertEqual(35237, solve2(text))


text = '''194, 200
299, 244
269, 329
292, 55
211, 63
123, 311
212, 90
292, 169
359, 177
354, 95
101, 47
95, 79
95, 287
294, 126
81, 267
330, 78
202, 165
225, 178
266, 272
351, 326
180, 62
102, 178
151, 101
343, 145
205, 312
74, 193
221, 56
89, 89
242, 172
59, 138
83, 179
223, 88
297, 234
147, 351
226, 320
358, 338
321, 172
54, 122
263, 165
126, 341
64, 132
264, 306
72, 202
98, 49
238, 67
310, 303
277, 281
222, 318
357, 169
123, 225'''