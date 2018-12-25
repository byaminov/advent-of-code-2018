import re

import numpy as np


def solve1(text: str):
    positions = []
    velocities = []
    # position=< 9,  1> velocity=< 0,  2>
    line_pattern = re.compile(r'position=<(.*)> velocity=<(.*)>')
    for line in text.split('\n'):
        if not line:
            continue
        m = line_pattern.match(line)
        s1, s2 = m.groups()
        x, y = map(lambda s: int(s.strip()), s1.split(', '))
        vx, vy = map(lambda s: int(s.strip()), s2.split(', '))
        positions.append((x, y))
        velocities.append((vx, vy))

    time = 0
    while True:
        time += 1
        for i in range(len(positions)):
            vx, vy = velocities[i]
            x, y = positions[i]
            x += vx
            y += vy
            positions[i] = (x, y)

        x0, y0 = positions[0]
        goes_right = (x0 + 1, y0) in positions and (x0 + 2, y0) in positions
        goes_left = (x0 - 1, y0) in positions and (x0 - 2, y0) in positions
        goes_up = (x0, y0 - 1) in positions and (x0, y0 - 2) in positions
        goes_down = (x0, y0 + 1) in positions and (x0, y0 + 2) in positions
        if goes_right or goes_left or goes_up or goes_down:
            draw(positions)
            input(f'time = {time}, continue?\n\n')


def draw(positions):
    max_x = max(map(lambda pos: pos[0], positions)) + 1
    max_y = max(map(lambda pos: pos[1], positions)) + 1
    min_x = min(map(lambda pos: pos[0], positions)) - 1
    min_y = min(map(lambda pos: pos[1], positions)) - 1
    grid = np.full([max_y - min_y, max_x - min_x], '.', dtype=np.object)
    for x, y in positions:
        grid[y - min_y, x - min_x] = 'x'

    np.set_printoptions(edgeitems=30, linewidth=100000)
    print(grid)
