from collections import defaultdict
from typing import List

import networkx as nx


def solve1(text: str):
    distances = populate_grid_and_get_distances(text)
    return max(distances.values())


def solve2(text: str):
    distances = populate_grid_and_get_distances(text)
    return len([d for d in distances.values() if d >= 1000])


def populate_grid_and_get_distances(text):
    grid = defaultdict(lambda: '?')
    pattern = text[1:-1]
    go(grid, (0, 0), pattern)
    # print_grid(grid)
    graph = create_graph(grid)
    distances = nx.shortest_path_length(graph, source=(0, 0), target=None)
    return distances


def print_grid(grid):
    min_y = min([y for y, x in grid])
    max_y = max([y for y, x in grid])
    min_x = min([x for y, x in grid])
    max_x = max([x for y, x in grid])
    for y in range(min_y, max_y + 1):
        line = [grid[(y, x)] if (y, x) != (0, 0) else 'X' for x in range(min_x, max_x + 1)]
        print(line)
    print()


def go(grid, pos, pattern):
    y, x = pos
    grid[(y, x)] = '.'

    for i, char in enumerate(pattern):
        if char in 'WESN':
            if char == 'W':
                grid[(y, x - 1)] = '|'
                grid[(y - 1, x - 1)] = '#'
                grid[(y + 1, x - 1)] = '#'
                x -= 2
            elif char == 'E':
                grid[(y, x + 1)] = '|'
                grid[(y - 1, x + 1)] = '#'
                grid[(y + 1, x + 1)] = '#'
                x += 2
            elif char == 'N':
                grid[(y - 1, x)] = '-'
                grid[(y - 1, x - 1)] = '#'
                grid[(y - 1, x + 1)] = '#'
                y -= 2
            elif char == 'S':
                grid[(y + 1, x)] = '-'
                grid[(y + 1, x - 1)] = '#'
                grid[(y + 1, x + 1)] = '#'
                y += 2
            grid[(y, x)] = '.'
        elif char == '(':
            routes, leftover = get_options(pattern[i:])
            route_ends = set()
            for route in routes:
                if route:
                    went_to = go(grid, (y, x), route)
                    route_ends = route_ends.union(went_to)
                else:
                    route_ends.add((y, x))
            final_ends = set()
            for route_end in route_ends:
                final_ends = final_ends.union(go(grid, route_end, leftover))
            return final_ends

        else:
            assert False

    return {(y, x)}


def create_graph(grid):
    g = nx.Graph()
    for (y, x), char in grid.items():
        if char == '|':
            g.add_edge((y, x - 1), (y, x + 1))
        elif char == '-':
            g.add_edge((y - 1, x), (y + 1, x))
    return g


def get_options(pattern_starting_with_paren) -> (List[str], str):
    # find matching )
    depth = 0
    last_start = 1
    parts = []
    j = 0
    for j, c in enumerate(pattern_starting_with_paren):
        if j == 0:
            continue
        if c == '(':
            depth += 1
        elif c == '|' and depth == 0:
            parts.append(pattern_starting_with_paren[last_start:j])
            last_start = j + 1
        elif c == ')':
            if depth == 0:
                parts.append(pattern_starting_with_paren[last_start:j])
                break
            else:
                depth -= 1
    assert j <= len(pattern_starting_with_paren)
    return parts, pattern_starting_with_paren[j + 1:]
