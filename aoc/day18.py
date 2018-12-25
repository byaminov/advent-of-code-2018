import numpy as np

from cycle_detector import CycleDetector


def solve1(text: str, after_minutes: int):
    lines = text.split('\n')
    width = len(lines[0])
    height = len(lines)
    grid = np.full([height, width], '', dtype=np.object)
    for y, line in enumerate(lines):
        if not line:
            continue
        for x, char in enumerate(line):
            grid[y, x] = char

    cd = CycleDetector(after_minutes)
    for minute in range(1, after_minutes + 1):
        grid = grow(grid)
        resource = (grid == '|').sum() * (grid == '#').sum()
        if cd.next_and_check(resource, minute):
            return cd.value_on_requested_iteration_


def grow(grid):
    new = np.full(grid.shape, '', dtype=np.object)
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            # an open acre can fill with trees,
            if grid[y, x] == '.':
                # An open acre will become filled with trees if three or more adjacent acres contained trees.
                # Otherwise, nothing happens.
                if count(grid, y, x, '|') >= 3:
                    new[y, x] = '|'
                else:
                    new[y, x] = '.'
            # a wooded acre can be converted to a lumberyard, or
            elif grid[y, x] == '|':
                # An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards.
                # Otherwise, nothing happens.
                if count(grid, y, x, '#') >= 3:
                    new[y, x] = '#'
                else:
                    new[y, x] = '|'
            # a lumberyard can be cleared to open ground
            elif grid[y, x] == '#':
                # An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one
                # other lumberyard and at least one acre containing trees. Otherwise, it becomes open.
                if count(grid, y, x, '#') >= 1 and count(grid, y, x, '|') >= 1:
                    new[y, x] = '#'
                else:
                    new[y, x] = '.'
    return new


def count(grid, start_y, start_x, value):
    result = 0
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if dy == 0 and dx == 0:
                continue
            y = start_y + dy
            x = start_x + dx
            if y not in range(grid.shape[0]):
                continue
            if x not in range(grid.shape[1]):
                continue
            if grid[y, x] == value:
                result += 1
    return result
