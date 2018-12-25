def solve1(text: str, generations=20):
    initial_state = text.split('\n')[0].replace('initial state: ', '')
    rules = dict()
    for line in all_rules().split('\n'):
        pattern, result = line.split(' => ')
        rules[pattern] = result
    for line in text.split('\n')[2:]:
        pattern, result = line.split(' => ')
        rules[pattern] = result

    initial_state = '.....' + initial_state + '.....'
    first_index = -5
    state = initial_state
    previous_result = 0
    for generation in range(generations):
        new_state = ['.'] * len(state)
        for i in range(len(state) - 4):
            grows = rules[state[i:i+5]]
            new_state[i+2] = grows
        state = ''.join(new_state)
        first_grows = state.index('#')
        to_add_left = 5 - first_grows
        if to_add_left > 0:
            state = ('.' * to_add_left) + state
            first_index -= to_add_left
        last_grows = state.rindex('#')
        to_add_right = 5 - (len(state) - 1 - last_grows)
        if to_add_right > 0:
            state = state + ('.' * to_add_right)

        result = 0
        for i, pot in enumerate(state):
            if pot == '#':
                result += (first_index + i)
        print('%d  result: %d  result diff: %d  plant width: %d' % (generation, result,
              result - previous_result, last_grows - first_grows))
        previous_result = result

    result = 0
    for i, pot in enumerate(state):
        if pot == '#':
            result += (first_index + i)
    return result


def all_rules():
    return '''####. => .
##.#. => .
.##.# => .
..##. => .
..... => .
.#.#. => .
.###. => .
.#.## => .
#.#.# => .
.#... => .
#..#. => .
....# => .
###.. => .
##..# => .
#..## => .
..#.. => .
##### => .
.#### => .
#.##. => .
#.### => .
...#. => .
###.# => .
#.#.. => .
##... => .
...## => .
.#..# => .
#.... => .
#...# => .
.##.. => .
..### => .
##.## => .
..#.# => .'''
