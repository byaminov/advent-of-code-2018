import unittest

from aoc.cycle_detector import *


class TestCycleDetector(unittest.TestCase):

    def test_cycle_length_3(self):
        values = [0, 1, 2, 3, 0, 2, 3, 0, 2]
        self.assertEqual(3, find_value_at(values, 10)[0])
        self.assertEqual(3, find_value_at(values, 16)[0])
        self.assertEqual(2, find_value_at(values, 99999999996)[0])
        self.assertEqual(3, find_value_at(values, 99999999997)[0])
        self.assertEqual(0, find_value_at(values, 99999999998)[0])
        self.assertEqual(2, find_value_at(values, 99999999999)[0])
        cd = find_value_at(values, 15)[1]
        self.assertEqual(3, cd.cycle_size_)
        self.assertEqual(2, cd.value_on_requested_iteration_)
        self.assertEqual(3, cd.iteration_of_first_cycle_start_)
        self.assertEqual([2, 3, 0], cd.cycle_)

    def test_cycle_length_1(self):
        values = [3] * 10
        value, cd = find_value_at(values, 10, min_cycle_size=1)
        self.assertEqual(3, value)
        self.assertEqual(1, cd.cycle_size_)
        self.assertEqual(1, cd.iteration_of_first_cycle_start_)

    def test_min_cycle_length(self):
        values = '0123_abCCCabCCCabCCCabCCCabCCC'

        # # with cycle size 1 "CCC" would be considered a cycle repetition
        value, cd = find_value_at(values, 27, min_cycle_size=1)
        self.assertEqual('C', value)
        self.assertEqual(1, cd.cycle_size_)
        self.assertEqual(8, cd.iteration_of_first_cycle_start_)
        self.assertEqual(['C'], cd.cycle_)

        # with cycle size > 1 "abCCC" would be considered a cycle
        value, cd = find_value_at(values, 27, min_cycle_size=2)
        self.assertEqual('b', value)
        self.assertEqual(5, cd.cycle_size_)
        self.assertEqual(6, cd.iteration_of_first_cycle_start_)
        self.assertEqual('abCCC', ''.join(cd.cycle_))

        # with cycle size > 5 "abCCCabCCC" would be considered a cycle
        # the return value would be still the same
        value, cd = find_value_at(values, 27, min_cycle_size=6)
        self.assertEqual('b', value)
        self.assertEqual(10, cd.cycle_size_)
        self.assertEqual(6, cd.iteration_of_first_cycle_start_)
        self.assertEqual('abCCCabCCC', ''.join(cd.cycle_))

    def test_early_stopping(self):
        values = '12345'
        value, cd = find_value_at(values, 3)
        self.assertEqual('3', value)
        self.assertEqual('3', cd.value_on_requested_iteration_)
        self.assertEqual(None, cd.cycle_size_)
        self.assertEqual(None, cd.cycle_)
        self.assertEqual(None, cd.iteration_of_first_cycle_start_)

    def test_usage_within_iteration(self):
        before_cycle = list(range(300, 0, -1))
        cycle = list(range(0, 401))

        cd = CycleDetector(return_value_for_iteration=len(before_cycle) + len(cycle) * 1000000 + 5,
                           max_cycle_size=500)
        i = 0
        while True:
            if i < len(before_cycle):
                value = before_cycle[i]
            else:
                value = cycle[(i - len(before_cycle)) % len(cycle)]
            if cd.next_and_check(value, i + 1):
                break
            i += 1

        self.assertEqual(4, cd.value_on_requested_iteration_)
        self.assertEqual(cycle, cd.cycle_)

    def test_no_return_requested(self):
        values = [0, 1, 2, 3, 0, 2, 3, 0, 2]
        cd = CycleDetector()
        for v in values:
            if cd.next_and_check(v):
                break

        self.assertEqual(3, cd.cycle_size_)
        self.assertEqual([2, 3, 0], cd.cycle_)
        self.assertEqual(None, cd.value_on_requested_iteration_)
