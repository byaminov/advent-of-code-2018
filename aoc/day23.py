import re

import networkx as nx

from aoc import search_minimum_matching


def solve1(text: str):
    nanobots = parse(text)
    nanobots.sort(reverse=True)
    strongest = nanobots[0]
    max_r, sx, sy, sz = strongest
    n_in_range_of_strongest = 0
    for _, x, y, z in nanobots:
        if dist(sx, sy, sz, x, y, z) <= max_r:
            n_in_range_of_strongest += 1
    return n_in_range_of_strongest


def parse(text):
    # pos=<0,0,0>, r=4
    line_pattern = re.compile(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(-?\d+)')
    lines = text.split('\n')
    nanobots = []
    for line in lines:
        if not line:
            continue
        m = line_pattern.match(line)
        x, y, z, r = list(map(int, m.groups()))
        nanobots.append((r, x, y, z))
    return nanobots


def solve2(text: str):
    nanobots = parse(text)
    intersections = create_intersections_graph(nanobots)

    # find the biggest subset of nanobots all intersecting with each other (clique in a graph)
    print('looking for cliques')
    max_subset = max(nx.find_cliques(intersections), key=len)
    print('found biggest clique of size', len(max_subset))
    return find_closest_point(max_subset)


def create_intersections_graph(nanobots):
    g = nx.Graph()
    for na in nanobots:
        for nb in nanobots:
            if na == nb:
                continue
            if intersects(na, nb):
                g.add_edge(na, nb)
    return g


def find_closest_point(nanobots):
    return search_minimum_matching(
        lambda r: all(intersects((r, 0, 0, 0), n) for n in nanobots),
        start_from=0
    )


def dist(sx, sy, sz, x, y, z):
    return abs(sx - x) + abs(sy - y) + abs(sz - z)


def intersects(na, nb):
    r1, sx, sy, sz = na
    r2, x, y, z = nb
    return dist(sx, sy, sz, x, y, z) <= r1 + r2
