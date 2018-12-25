import re
from collections import defaultdict, deque


def solve1(text: str, count_chars='|~'):
    grid, bounds = parse(text)
    min_y, max_y, min_x, max_x = bounds

    expand(grid, bounds)

    n_water = 0
    for y in range(min_y, max_y + 1):
        if y == 0:
            continue
        for x in range(min_x - 1, max_x + 2):
            if grid[(y, x)] in count_chars:
                n_water += 1

    # print_grid(grid, bounds)

    return n_water


def parse(text):
    # x=495, y=2..7
    # y=7, x=495..501
    line_pattern = re.compile(r'(\w)=(\d+), (\w)=(\d+)\.\.(\d+)')
    lines = text.split('\n')
    grid = defaultdict(lambda: '.')
    for line in lines:
        if not line:
            continue
        m = line_pattern.match(line)
        a, a_value, b, b_from, b_to = m.groups()
        if a == 'x':
            x = int(a_value)
            for y in range(int(b_from), int(b_to) + 1):
                grid[(y, x)] = '#'
        else:
            y = int(a_value)
            for x in range(int(b_from), int(b_to) + 1):
                grid[(y, x)] = '#'
    max_y = max([y for y, x in grid])
    min_y = min([y for y, x in grid])
    max_x = max([x for y, x in grid])
    min_x = min([x for y, x in grid])
    bounds = min_y, max_y, min_x, max_x
    grid[(0, 500)] = '|'
    return grid, bounds


def expand(grid, bounds):
    min_y, max_y, min_x, max_x = bounds
    q = deque()
    q.append((0, 500))
    while q:
        y, x = q.popleft()

        if y < 0 or y > max_y or x < min_x - 1 or x > max_x + 1:
            # out of range
            continue
        if grid[(y, x)] != '|':
            # changed in the meanwhile
            continue
        below = grid[(y + 1, x)]
        if below == '|':
            # falling water
            continue

        # try going down
        if below == '.':
            grid[(y + 1, x)] = '|'
            q.append((y + 1, x))
        elif below in '#~':
            # go left
            left = grid[(y, x - 1)]
            if left == '.':
                grid[(y, x - 1)] = '|'
                q.append((y, x - 1))
            # and right
            right = grid[(y, x + 1)]
            if right == '.':
                grid[(y, x + 1)] = '|'
                q.append((y, x + 1))
            if left != '.' and right != '.':
                # did not go left or right, check if it is a filled level
                clays_left = [xx for xx in range(min_x, x) if grid[(y, xx)] == '#']
                clays_right = [xx for xx in range(x + 1, max_x + 1) if grid[(y, xx)] == '#']
                if clays_left and clays_right:
                    first_clay_left = max(clays_left)
                    first_clay_right = min(clays_right)
                    is_water = [grid[(y, xx)] in '|~'
                                for xx in range(first_clay_left + 1, first_clay_right)]
                    if all(is_water):
                        # is standing water
                        for xx in range(first_clay_left + 1, first_clay_right):
                            grid[(y, xx)] = '~'
                            if grid[(y - 1, xx)] == '|':
                                q.append((y - 1, xx))


def print_grid(grid, bounds):
    min_y, max_y, min_x, max_x = bounds
    lines = []
    for y in range(min(min_y - 1, 0), max_y + 2):
        lines.append(''.join([grid[(y, x)] for x in range(min_x - 2, max_x + 3)]))
    print('\n'.join(lines) + '\n')
