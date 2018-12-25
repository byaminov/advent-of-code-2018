from collections import deque

import numpy as np


def solve1(serial):
    grid = np.full([300, 300], 0)
    for x in range(300):
        for y in range(300):
            grid[y, x] = power(x + 1, y + 1, serial)

    max_sum = -10000
    max_xy = None
    for x in range(298):
        for y in range(298):
            xy_sum = grid[y:y + 3, x:x + 3].sum()
            if xy_sum > max_sum:
                max_sum = xy_sum
                max_xy = (x, y)

    return max_xy[0] + 1, max_xy[1] + 1


def power(x, y, serial):
    """
    For example, to find the power level of the fuel cell at 3,5 in a grid with serial number 8:

    The rack ID is 3 + 10 = 13.
    The power level starts at 13 * 5 = 65.
    Adding the serial number produces 65 + 8 = 73.
    Multiplying by the rack ID produces 73 * 13 = 949.
    The hundreds digit of 949 is 9.
    Subtracting 5 produces 9 - 5 = 4.
    So, the power level of this fuel cell is 4.
    """
    rack_id = x + 10
    result = rack_id * y
    result += serial
    result *= rack_id
    if result >= 100:
        result = (result % 1000) // 100
    else:
        result = 0
    result -= 5
    return result


def solve2(serial):
    grid = np.full([300, 300], 0)
    for x in range(300):
        for y in range(300):
            grid[y, x] = power(x + 1, y + 1, serial)

    max_sum = -10000
    max_xyw = None

    last_sums = deque()
    max_decreasing_ws = 10

    for w in range(1, 300):
        print('at w =', w)
        max_sum_per_w = None
        for x in range(0, 301 - w):
            for y in range(0, 301 - w):
                xyw_sum = grid[y:y + w, x:x + w].sum()
                if xyw_sum > max_sum:
                    max_sum = xyw_sum
                    max_xyw = (x, y, w)
                if not max_sum_per_w or xyw_sum > max_sum_per_w:
                    max_sum_per_w = xyw_sum

        last_sums.append(max_sum_per_w)
        if len(last_sums) > max_decreasing_ws:
            last_sums.popleft()
        if len(last_sums) == max_decreasing_ws and \
                list(last_sums) == sorted(last_sums, reverse=True):
            # decreasing all the time
            print(f'sums have been decreasing the last {max_decreasing_ws} window sizes, aborting.')
            print('max_sum =', max_sum)
            return max_xyw[0] + 1, max_xyw[1] + 1, max_xyw[2]

    print('max_sum=', max_sum)
    return max_xyw[0] + 1, max_xyw[1] + 1, max_xyw[2]
