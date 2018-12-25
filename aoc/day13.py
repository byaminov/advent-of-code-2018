def solve1(text: str):
    carts, tracks, max_width = parse(text)

    tick = 0
    while True:
        carts_sorted = list(carts.items())
        carts_sorted.sort(key=lambda id_data: id_data[1][0][0] * max_width + id_data[1][0][1])
        for cart_id, cart_data in carts_sorted:
            if cart_id not in carts:
                print('skipping as its already collided', cart_id)
                continue

            position, direction, turn = cart_data

            new_direction, new_position, new_turn = move_and_turn(position, direction, turn, tracks)

            carts_at_new_position = [c for c in carts.items() if c[1][0] == new_position]
            if carts_at_new_position:
                return tuple(reversed(new_position))
            else:
                carts[cart_id] = new_position, new_direction, new_turn

        tick += 1


def solve2(text: str):
    carts, tracks, max_width = parse(text)

    tick = 0
    while True:
        carts_sorted = list(carts.items())
        carts_sorted.sort(key=lambda id_data: id_data[1][0][0] * max_width + id_data[1][0][1])
        for cart_id, cart_data in carts_sorted:
            if cart_id not in carts:
                continue

            position, direction, turn = cart_data

            new_direction, new_position, new_turn = move_and_turn(position, direction, turn, tracks)

            carts_at_new_position = [c for c in carts.items() if c[1][0] == new_position]
            if carts_at_new_position:
                collided_with = carts_at_new_position[0]
                del carts[cart_id]
                del carts[collided_with[0]]
            else:
                carts[cart_id] = new_position, new_direction, new_turn

        tick += 1

        if len(carts) == 1:
            pos, direction, turn = list(carts.values())[0]
            return tuple(reversed(pos))


def parse(text):
    tracks = text.split('\n')
    carts = dict()
    cart_id = 0
    max_width = 0
    for y, row in enumerate(tracks):
        max_width = max(len(row), max_width)
        for x, char in enumerate(row):
            if char in ['v', '^', '>', '<']:
                carts[cart_id] = ((y, x), char, 'left')
                cart_id += 1
                if char in ['>', '<']:
                    tracks[y] = tracks[y][:x] + '-' + tracks[y][x + 1:]
                else:
                    tracks[y] = tracks[y][:x] + '|' + tracks[y][x + 1:]
    return carts, tracks, max_width


def move_and_turn(position, d, turn, tracks):
    y, x = position

    # first go
    if d == '^':
        new_yx = y - 1, x
    elif d == 'v':
        new_yx = y + 1, x
    elif d == '>':
        new_yx = y, x + 1
    elif d == '<':
        new_yx = y, x - 1
    else:
        assert False

    # then turn
    track = tracks[new_yx[0]][new_yx[1]]
    new_turn = turn
    if track == '+':
        if turn == 'left':
            d = {
                '^': '<',
                '<': 'v',
                'v': '>',
                '>': '^'
            }[d]
            new_turn = 'straight'
        elif turn == 'straight':
            new_turn = 'right'
        elif turn == 'right':
            d = {
                '^': '>',
                '>': 'v',
                'v': '<',
                '<': '^'
            }[d]
            new_turn = 'left'
        else:
            assert False
    elif track == '/':
        d = {
            '^': '>',
            '>': '^',
            'v': '<',
            '<': 'v'
        }[d]
    elif track == '\\':
        d = {
            '^': '<',
            '>': 'v',
            'v': '>',
            '<': '^'
        }[d]

    return d, new_yx, new_turn
