import networkx as nx
import numpy as np


def solve1(depth, target):
    grid = create_grid(depth, target)
    return grid[0:target[0] + 1, 0:target[1] + 1].sum()


def solve2(depth, target):
    grid = create_grid(depth, target, (target[0] * 3, target[1] * 3))
    graph = create_graph(grid)
    return nx.shortest_path_length(graph,
                                   (0, 0, 't'),
                                   (target[0], target[1], 't'),
                                   weight='minutes')


def create_graph(grid):
    g = nx.DiGraph()
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            for tool in 'tgn':
                current_region = grid[x, y]
                if is_allowed(tool, current_region):
                    current_node = (x, y, tool)
                    g.add_node(current_node)
                    # you can go to another cell
                    for target in get_around(grid, x, y):
                        target_region = grid[target[0], target[1]]
                        if is_allowed(tool, target_region):
                            target_node = (target[0], target[1], tool)
                            g.add_edge(current_node, target_node, minutes=1)
                    # or you can change the tool
                    for new_tool in 'tgn':
                        if is_allowed(new_tool, current_region):
                            target_node = (x, y, new_tool)
                            g.add_edge(current_node, target_node, minutes=7)

    return g


def is_allowed(tool, region):
    if region == 0:
        return tool in 'tg'
    if region == 1:
        return tool in 'gn'
    return tool in 'tn'


def get_around(grid, x, y):
    result = []
    if x > 0:
        result.append((x - 1, y))
    if x < grid.shape[0] - 1:
        result.append((x + 1, y))
    if y > 0:
        result.append((x, y - 1))
    if y < grid.shape[1] - 1:
        result.append((x, y + 1))
    return result


def create_grid(depth, target, bounds=None):
    if not bounds:
        bounds = target
    g_index = np.full([bounds[0] + 1, bounds[1] + 1], -1, dtype=np.int64)
    erosion = np.full([bounds[0] + 1, bounds[1] + 1], -1, dtype=np.int64)

    for x in range(g_index.shape[0]):
        for y in range(g_index.shape[1]):
            if (x, y) == (0, 0):
                g_index[x, y] = 0
            elif (x, y) == target:
                g_index[x, y] = 0
            elif y == 0:
                g_index[x, y] = (x * 16807) % 20183
            elif x == 0:
                g_index[x, y] = (y * (48271 % 20183)) % 20183
            else:
                g_index[x, y] = (erosion[x - 1, y] * erosion[x, y - 1]) % 20183

            erosion[x, y] = (g_index[x, y] + depth) % 20183

    types = erosion % 3
    return types
