from collections import defaultdict, Counter


def solve1(text: str):
    points, grid_max, grid_min = parse_points(text)

    grid = dict()

    for x in range(grid_min[0], grid_max[0]):
        for y in range(grid_min[1], grid_max[1]):
            closest = find_closest(x, y, points)
            if len(closest) == 1:
                grid[(x, y)] = closest[0]
            elif len(closest) > 1:
                grid[(x, y)] = '.'
            else:
                raise ValueError(f'something is wrong for {x}, {y}: {closest}')

    border_ids = set()
    for x in range(grid_min[0], grid_max[0]):
        border_ids.add(grid[(x, grid_min[1])])
        border_ids.add(grid[(x, grid_max[1]-1)])
    for y in range(grid_min[1], grid_max[1]):
        border_ids.add(grid[(grid_min[0], y)])
        border_ids.add(grid[(grid_max[0]-1, y)])

    counter = Counter(grid.values())
    for id_, area in counter.most_common():
        if id_ not in border_ids:
            return area


def parse_points(text):
    points = list()
    for line in text.split('\n'):
        x, y = line.split(', ')
        points.append((int(x), int(y)))

    max_x = max(p[0] for p in points)
    min_x = min(p[0] for p in points)
    max_y = max(p[1] for p in points)
    min_y = min(p[1] for p in points)

    width, height = max_x - min_x, max_y - min_y

    grid_min = (min_x - width, min_y - height)
    grid_max = (max_x + width + 1, max_y + height + 1)

    return points, grid_max, grid_min


def find_closest(start_x, start_y, points):
    distances = defaultdict(list)
    min_dist = 20000

    for i, p in enumerate(points):
        id_ = str(i)
        dist = abs(p[0] - start_x) + abs(p[1] - start_y)
        distances[dist].append(id_)
        if dist < min_dist:
            min_dist = dist

    return distances[min_dist]


def solve2(text: str, max_distance=10000):
    points, grid_max, grid_min = parse_points(text)

    count = 0

    for x in range(grid_min[0], grid_max[0]):
        for y in range(grid_min[1], grid_max[1]):
            total_distance = find_total_distance(x, y, points)
            if total_distance < max_distance:
                count += 1

    return count


def find_total_distance(start_x, start_y, points):
    total = 0
    for p in points:
        dist = abs(p[0] - start_x) + abs(p[1] - start_y)
        total += dist
    return total
