from collections import Counter
from itertools import combinations


def solve1(text: str):
    twos = 0
    threes = 0
    for line in text.split('\n'):
        c = Counter(line)
        if 2 in c.values():
            twos += 1
        if 3 in c.values():
            threes += 1
    return twos * threes


def solve2(text: str):
    for id1, id2 in combinations(text.split('\n'), r=2):
        matches = list(map(lambda cs: 0 if cs[0] == cs[1] else 1, zip(id1, id2)))
        if sum(matches) == 1:
            non_matching = matches.index(1)
            return id1[:non_matching] + id1[non_matching+1:]
    return ''


