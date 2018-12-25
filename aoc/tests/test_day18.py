import unittest

from aoc.day18 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        print('Testing')
        self.assertEqual(1147, solve1('''.#.#...|#.
.....#|##|
.|..|...#.
..|#.....#
#.#|||#|#|
...#.||...
.|....|...
||...#|.#|
|.||||..|.
...#.|..|.''', after_minutes=10))
        print('Solving 1')
        self.assertEqual(737800, solve1(text, after_minutes=10))

    def test_solve2(self):
        print('Solving 2')
        self.assertEqual(212040, solve1(text, after_minutes=1000000000))


text = '''.#||#|||##....|..#......|..#...##..|#....#|.......
|..#..#....|.#|.|......||.|..#|...||#......|.....|
..#|##.#.#.##...#..........#.#|...||.|..|##.#.|.||
|.#.#|#.#.||...|...|||#|.#..#|..|#.#..##.|......#|
#..|#|........|......##.|##..|..#|...#||.......|#.
#...|#..#......##...##.|......|.#|#.|..|#.|#...|.#
|#.....|.|.###..#...|....|..|.....|#..#..|.......#
.....##.|........|...#...|#..|..##...|......||.|..
#....#..|..#.........||.##..##|#.##.#....|...#.|.|
...|..#.|.|#||..|#.||.....#|.#|.|#|.....#|#.###|##
...|..#.||....||.#.|....|#...#|.||#.#..#...#...##.
...||.|#......|...|#...#..|...||..|.#|.....##.|||.
...|.#|.|#.|...#.....|.|...#|.|.........|||.|.##.|
..|..|#..|........#.|#.||.#|..#.|....||...|.|.#...
.|.|...#.|.#..........|..|........#|.|....|..|....
|...|.#..|..||#.||#........|...|.|.|..|.#|..|...|.
..#.#..#|......#|.#....###...#.#..|..|.....|....#.
..|||..#...|#|.##..#|#.#.#..|......#.....||.##.##.
...|...#.|##..|..|.|.#.|||#|......|.|..|.||#.#..||
||.....|..#|.#...|.|.#.||.....##...|.#...|#.#.##..
.|.|.#|..#........#..||.|.#|...###|.#..#........||
|.##......|.|||..|...##.|.....#|||....#...#||||.|.
...#...|||.......#..|.#.||.|.......|#|..|..#.|....
|..|#.............|...##|....|.#|..|#...|#...|.|..
|.|....|#...|##...#.....|..|..|...||#..|...|.#..||
...|.##.##....#.|#......##|...|..#.#....||||.||||.
||.#....#..#...|.||||##.....#..##......#..||##.#..
........#....|..#..#|#|....#..|..#.....##|...#.|..
..#.|#.|.#.#..#.....|..#...###....|#...........#.|
#.|#|.#...|.#.#.|..|....|..|.|.#|.#|#.............
.||......|||||...||.#......|#...|#.|.|..#.|.#|....
|.#|.#.|#.#..#.##......#.#|#.....#..#....#.##|.#..
#.#..|....###..|..|.||..|#..|...|...#|##....|#.#..
.|#...|..#|..#.|||.|..||...|..#.#...|..|#......#..
.##...#||..|#.#...|.......|.##.....|..|.#..|.#.|.#
#||##....#.|.||.#....|.#|..|.|.#....#..#...||.....
......||.#|........#....||.##...#....|.||...|..##|
#........|..#|.......#.#.#|..|...#..||||...|.....#
....#||.##....|..##...##|.....|..#.#.....#..|.....
.|.|#....|..|.#|#....#..|...|..#|#...#.||...#.#...
#....|.|#||....#.#|#|.#..|.#.....##........|...|#.
#...#...|..|.#....|..|.#....#.|#...#...#|.|.#.....
....#.......#....##|.#.|....##..|||##.....#|.....#
.....||||..|.#|#..|...|.#..|...#|...|.##||.#||....
.||....#...|..#.|#.#.|#|#|..#.........##...||..|#.
...|.#.#..........##...#|...|.##.|.|.||.#......#..
...###.#..|..#.....#|#.#.|#.######|.|#.....###.|.#
..##.....##...|..|....#|..||....|.|....#..|...|..#
.|.##.#...|.|.||.||.|#.#.....||#.#|.#|.|..#|.#..|#
.|...............#.#..#.##......#|||.|..||..#....#'''