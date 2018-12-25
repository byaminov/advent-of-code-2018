import re
from collections import defaultdict

import networkx as nx


def solve1(text: str):
    tree = nx.DiGraph()
    for s1, s2 in parse_dependencies(text):
        tree.add_edge(s1, s2)

    nodes = list(nx.lexicographical_topological_sort(tree))
    return ''.join(nodes)


def parse_dependencies(text: str):
    line_pattern = re.compile(r'Step (\w+) must be finished before step (\w+) can begin.')
    dependencies = []
    for line in text.split('\n'):
        m = line_pattern.match(line)
        s1, s2 = m.groups()
        dependencies.append((s1, s2))
    return dependencies


def solve2(text: str, extra_duration=60, n_workers=5):
    requirements = defaultdict(list)
    all_tasks = set()

    for s1, s2 in parse_dependencies(text):
        requirements[s2].append(s1)
        all_tasks.add(s1)
        all_tasks.add(s2)

    cost = dict()
    for n in all_tasks:
        cost[n] = ord(n) - 64 + extra_duration

    workers = dict()
    for i in range(n_workers):
        workers[i] = dict()

    result = ''
    done = set()
    working = set()
    total_time = 0
    while len(done) < len(all_tasks):
        total_time += 1
        # run work
        for worker, work in workers.items():
            if work:
                item, time = list(work.items())[0]
                if time <= 1:
                    # item is ready
                    for req in requirements.values():
                        if item in req:
                            req.remove(item)
                    result += item
                    done.add(item)
                    working.remove(item)
                    del work[item]
                else:
                    work[item] -= 1

        # add work
        ready_to_start = set(filter(lambda c: not requirements[c], all_tasks)) - done - working
        ready_to_start = sorted(list(ready_to_start))
        free_workers = list()
        for worker, work in workers.items():
            if not work:
                free_workers.append(worker)
        for i, item in enumerate(ready_to_start[:len(free_workers)]):
            workers[free_workers[i]][item] = cost[item]
            working.add(item)

    return total_time - 1
