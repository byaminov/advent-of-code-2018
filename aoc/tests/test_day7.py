import unittest

from aoc.day7 import *


class TestSolution(unittest.TestCase):

    def test_solve1(self):
        self.assertEqual('CABDFE', solve1('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.'''))
        self.assertEqual('ACBDESULXKYZIMNTFGWJVPOHRQ', solve1(text))

    def test_solve2(self):
        self.assertEqual(15, solve2('''Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.''', extra_duration=0, n_workers=2))
        self.assertEqual(980, solve2(text))


text = '''Step U must be finished before step R can begin.
Step C must be finished before step B can begin.
Step A must be finished before step S can begin.
Step E must be finished before step O can begin.
Step D must be finished before step Z can begin.
Step L must be finished before step X can begin.
Step S must be finished before step F can begin.
Step B must be finished before step J can begin.
Step Z must be finished before step T can begin.
Step X must be finished before step W can begin.
Step K must be finished before step T can begin.
Step M must be finished before step H can begin.
Step I must be finished before step W can begin.
Step T must be finished before step J can begin.
Step N must be finished before step O can begin.
Step F must be finished before step G can begin.
Step W must be finished before step P can begin.
Step G must be finished before step V can begin.
Step Y must be finished before step V can begin.
Step J must be finished before step V can begin.
Step V must be finished before step R can begin.
Step P must be finished before step H can begin.
Step O must be finished before step R can begin.
Step H must be finished before step R can begin.
Step R must be finished before step Q can begin.
Step L must be finished before step O can begin.
Step V must be finished before step H can begin.
Step X must be finished before step K can begin.
Step D must be finished before step N can begin.
Step C must be finished before step P can begin.
Step E must be finished before step I can begin.
Step P must be finished before step O can begin.
Step T must be finished before step F can begin.
Step U must be finished before step K can begin.
Step A must be finished before step O can begin.
Step G must be finished before step O can begin.
Step A must be finished before step W can begin.
Step G must be finished before step Q can begin.
Step U must be finished before step J can begin.
Step V must be finished before step O can begin.
Step J must be finished before step Q can begin.
Step X must be finished before step G can begin.
Step B must be finished before step Y can begin.
Step J must be finished before step R can begin.
Step B must be finished before step F can begin.
Step K must be finished before step F can begin.
Step S must be finished before step Z can begin.
Step T must be finished before step H can begin.
Step W must be finished before step R can begin.
Step I must be finished before step N can begin.
Step Z must be finished before step R can begin.
Step J must be finished before step O can begin.
Step M must be finished before step R can begin.
Step Y must be finished before step J can begin.
Step E must be finished before step J can begin.
Step T must be finished before step G can begin.
Step T must be finished before step V can begin.
Step M must be finished before step O can begin.
Step C must be finished before step J can begin.
Step D must be finished before step O can begin.
Step F must be finished before step P can begin.
Step H must be finished before step Q can begin.
Step F must be finished before step J can begin.
Step Z must be finished before step P can begin.
Step T must be finished before step O can begin.
Step Z must be finished before step M can begin.
Step U must be finished before step H can begin.
Step W must be finished before step J can begin.
Step L must be finished before step Y can begin.
Step A must be finished before step T can begin.
Step M must be finished before step V can begin.
Step O must be finished before step Q can begin.
Step N must be finished before step J can begin.
Step A must be finished before step V can begin.
Step K must be finished before step G can begin.
Step N must be finished before step F can begin.
Step B must be finished before step T can begin.
Step I must be finished before step H can begin.
Step V must be finished before step P can begin.
Step E must be finished before step T can begin.
Step E must be finished before step G can begin.
Step U must be finished before step L can begin.
Step X must be finished before step P can begin.
Step L must be finished before step R can begin.
Step Y must be finished before step O can begin.
Step K must be finished before step O can begin.
Step Z must be finished before step I can begin.
Step P must be finished before step R can begin.
Step A must be finished before step X can begin.
Step O must be finished before step H can begin.
Step C must be finished before step D can begin.
Step D must be finished before step F can begin.
Step X must be finished before step H can begin.
Step D must be finished before step Y can begin.
Step Y must be finished before step P can begin.
Step E must be finished before step V can begin.
Step K must be finished before step H can begin.
Step M must be finished before step G can begin.
Step L must be finished before step I can begin.
Step D must be finished before step K can begin.
Step D must be finished before step M can begin.'''
