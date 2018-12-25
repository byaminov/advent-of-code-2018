import networkx as nx
import numpy as np

from aoc import search_minimum_matching

np.set_printoptions(edgeitems=30, linewidth=100000)


def solve1(text: str, elf_power=3):
    lines = text.split('\n')
    grid = np.full([len(lines), len(lines[0])], '', dtype=np.object)
    last_id = 0
    for y, line in enumerate(lines):
        if not line:
            continue
        for x, char in enumerate(line):
            if char in ['G', 'E']:
                grid[y, x] = f'{char},200,{last_id}'
                last_id += 1
            else:
                grid[y, x] = char

    round_number = 0
    while True:

        moved_ids = set()
        for turn_y in range(grid.shape[0]):
            for turn_x in range(grid.shape[1]):
                y, x = turn_y, turn_x
                if grid[y, x] in ['#', '.']:
                    continue
                unit_type, hp, unit_id = grid[y, x].split(',')
                if unit_id in moved_ids:
                    continue
                moved_ids.add(unit_id)

                # find enemies
                enemy_type = 'E' if unit_type == 'G' else 'G'
                enemy_coords = find_units_coords(grid, enemy_type)
                if not enemy_coords:
                    # end of game
                    ally_hps = 0
                    for ally_y, ally_x in find_units_coords(grid, unit_type):
                        ally_hps += int(grid[ally_y, ally_x].split(',')[1])
                    return ally_hps * round_number

                # check if already in range
                adj_enemy_coords = None
                for adj_y, adj_x in around(y, x, grid):
                    if grid[adj_y, adj_x].startswith(enemy_type):
                        adj_enemy_coords = (adj_y, adj_x)
                        break

                if not adj_enemy_coords:
                    # move
                    in_range = find_in_range(enemy_coords, grid)

                    graph = create_graph(grid, y, x, in_range)

                    in_range_distances = sorted([(
                        nx.shortest_path_length(graph, (y, x), target),
                        target
                    ) for target in in_range if nx.has_path(graph, (y, x), target)])

                    if not in_range_distances:
                        # no reach to any enemies
                        continue

                    chosen_target = in_range_distances[0][1]

                    possible_moves = [pos for pos in around(y, x, grid) if grid[pos[0], pos[1]] == '.']
                    possible_move_distances = [(
                        nx.shortest_path_length(graph, move, chosen_target),
                        move
                    ) for move in possible_moves]

                    move_to = sorted(possible_move_distances)[0][1]

                    # go by the path
                    grid[y, x] = '.'
                    grid[move_to[0], move_to[1]] = f'{unit_type},{hp},{unit_id}'
                    y, x = move_to

                # attack
                weakest_hp = 10000
                adj_enemy_coords = None
                for adj_y, adj_x in around(y, x, grid):
                    if grid[adj_y, adj_x].startswith(enemy_type):
                        enemy_hp = int(grid[adj_y, adj_x].split(',')[1])
                        if enemy_hp < weakest_hp:
                            weakest_hp = enemy_hp
                            adj_enemy_coords = adj_y, adj_x

                if adj_enemy_coords:
                    # do attack
                    _, enemy_hp, enemy_id = grid[adj_enemy_coords[0], adj_enemy_coords[1]].split(',')
                    if unit_type == 'E':
                        enemy_hp = int(enemy_hp) - elf_power
                    else:
                        enemy_hp = int(enemy_hp) - 3
                    if enemy_hp <= 0:
                        grid[adj_enemy_coords[0], adj_enemy_coords[1]] = '.'
                        if unit_type == 'G' and elf_power > 3:  # mode 2 game
                            return 'elf died'
                    else:
                        grid[adj_enemy_coords[0], adj_enemy_coords[1]] = f'{enemy_type},{enemy_hp},{enemy_id}'

        round_number += 1


def find_in_range(enemy_coords, grid):
    return list({c for enemy in enemy_coords for c in around(enemy[0], enemy[1], grid) if grid[c[0], c[1]] == '.'})


def create_graph(grid, start_y, start_x, targets):
    g = nx.Graph()
    for y in range(grid.shape[0]):
        for x in range(grid.shape[1]):
            if grid[y, x] == '.' or \
                    (y == start_y and x == start_x) or \
                    ((y, x) in targets):
                g.add_node((y, x))
                for adj_y, adj_x in around(y, x, grid):
                    if grid[adj_y, adj_x] == '.' or \
                            (adj_y == start_y and adj_x == start_x) or \
                            ((adj_y, adj_x) in targets):
                        g.add_edge((y, x), (adj_y, adj_x))
    return g


def find_units_coords(grid, unit_type):
    return [(y, x) for y in range(grid.shape[0])
            for x in range(grid.shape[1])
            if grid[y, x].startswith(unit_type)]


def around(y, x, grid):
    result = []
    if y > 0:
        result.append((y - 1, x))
    if x > 0:
        result.append((y, x - 1))
    if x < grid.shape[1] - 1:
        result.append((y, x + 1))
    if y < grid.shape[0] - 1:
        result.append((y + 1, x))
    return result


def solve2(text: str):
    def try_with_power(power):
        print('playing with elf power', power)
        return solve1(text, elf_power=power) != 'elf died'

    minimum_power = search_minimum_matching(predicate=try_with_power, start_from=4)
    return solve1(text, minimum_power)
