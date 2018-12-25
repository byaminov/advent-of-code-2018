import re
from collections import defaultdict


def solve1(text: str):
    fabric = defaultdict(int)
    for claim_id, left, top, width, height in parse_claims(text):
        for x in range(left + 1, left + 1 + width):
            for y in range(top + 1, top + 1 + height):
                fabric[(y, x)] += 1
    return len(list(filter(lambda c: c > 1, fabric.values())))


def parse_claims(text: str):
    # #1 @ 1,3: 4x4
    pattern = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')
    claims = []
    for line in text.split('\n'):
        m = pattern.match(line)
        claim_id, left, top, width, height = list(map(int, m.groups()))
        claims.append((claim_id, left, top, width, height))
    return claims


def solve2(text: str):
    claims = parse_claims(text)
    all_ids = {c[0] for c in claims}
    overlapping_ids = set()

    ids = defaultdict(list)
    for claim_id, left, top, width, height in claims:
        for x in range(left + 1, left + 1 + width):
            for y in range(top + 1, top + 1 + height):
                if not ids[(y, x)]:
                    ids[(y, x)].append(claim_id)
                else:
                    ids[(y, x)].append(claim_id)
                    for cell_ids in ids[(y, x)]:
                        overlapping_ids.add(cell_ids)

    return list(all_ids - overlapping_ids)[0]
