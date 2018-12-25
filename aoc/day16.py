from typing import List
import networkx as nx

all_opcodes = [
    'addr', 'addi',
    'mulr', 'muli',
    'banr', 'bani',
    'borr', 'bori',
    'setr', 'seti',
    'gtir', 'gtri', 'gtrr',
    'eqir', 'eqri', 'eqrr'
]


def solve1(text: str):
    lines = text.splitlines()
    samples = 0
    for i in range(0, len(lines), 4):
        if lines[i].startswith('Before'):
            number, names = find_possible_opcodes(lines[i:i + 3])
            if len(names) >= 3:
                samples += 1
        else:
            break

    return samples


def solve2(text: str):
    possible_opcodes = dict()
    lines = text.splitlines()
    last_example_index = None
    for i in range(0, len(lines), 4):
        if lines[i].startswith('Before'):
            number, names = find_possible_opcodes(lines[i:i + 3])
            if number not in possible_opcodes:
                possible_opcodes[number] = names
            else:
                intersected = possible_opcodes[number].intersection(names)
                possible_opcodes[number] = intersected
        else:
            last_example_index = i
            break

    g = nx.DiGraph()
    g.add_nodes_from(possible_opcodes.keys(), bipartite=0)
    g.add_nodes_from(all_opcodes, bipartite=1)
    for number, names in possible_opcodes.items():
        for name in names:
            g.add_edge(number, name)
    matching = nx.bipartite.hopcroft_karp_matching(g)
    number_to_name = {n: o for n, o in matching.items() if isinstance(n, int)}

    rs = [0, 0, 0, 0]
    for line in lines[last_example_index:]:
        if not line:
            continue
        op_number, a, b, c = list(map(int, line.split(' ')))
        opcode = number_to_name[op_number]
        rs = run_opcode(opcode, a, b, c, rs)

    return rs[0]


def run_opcode(name: str, a: int, b: int, c: int, rs: List[int]) -> List[int]:
    rs = rs.copy()
    if name == 'addr':
        rs[c] = rs[a] + rs[b]
    elif name == 'addi':
        rs[c] = rs[a] + b
    elif name == 'mulr':
        rs[c] = rs[a] * rs[b]
    elif name == 'muli':
        rs[c] = rs[a] * b
    elif name == 'banr':
        rs[c] = rs[a] & rs[b]
    elif name == 'bani':
        rs[c] = rs[a] & b
    elif name == 'borr':
        rs[c] = rs[a] | rs[b]
    elif name == 'bori':
        rs[c] = rs[a] | b
    elif name == 'setr':
        rs[c] = rs[a]
    elif name == 'seti':
        rs[c] = a
    elif name == 'gtrr':
        rs[c] = 1 if rs[a] > rs[b] else 0
    elif name == 'gtir':
        rs[c] = 1 if a > rs[b] else 0
    elif name == 'gtri':
        rs[c] = 1 if rs[a] > b else 0
    elif name == 'eqrr':
        rs[c] = 1 if rs[a] == rs[b] else 0
    elif name == 'eqir':
        rs[c] = 1 if a == rs[b] else 0
    elif name == 'eqri':
        rs[c] = 1 if rs[a] == b else 0
    else:
        raise ValueError('unexpected opcode: ' + name)
    return rs


def find_possible_opcodes(lines: List[str]):
    # Before: [3, 2, 1, 1]
    # 9 2 1 2
    # After:  [3, 2, 2, 1]
    rs_before = list(map(int, lines[0][9:-1].split(', ')))
    rs_after = list(map(int, lines[2][9:-1].split(', ')))
    op = list(map(int, lines[1].split(' ')))
    op_number, a, b, c = op

    names = {name for name in all_opcodes
             if rs_after == run_opcode(name, a, b, c, rs_before)}

    return op_number, names
