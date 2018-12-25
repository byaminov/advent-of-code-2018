
def solve1(after_n_recipes):
    i1 = 0
    i2 = 1
    scores = [3, 7]

    while True:
        new_scores = str(scores[i1] + scores[i2])
        for s in new_scores:
            scores.append(int(s))
            if len(scores) >= after_n_recipes + 10:
                return ''.join(map(str, scores[-10:]))
        i1 = (i1 + scores[i1] + 1) % len(scores)
        i2 = (i2 + scores[i2] + 1) % len(scores)


def solve2(sequence):
    i1 = 0
    i2 = 1
    scores = [3, 7]
    sequence = str(sequence)

    while True:
        new_scores = str(scores[i1] + scores[i2])
        for s in new_scores:
            scores.append(int(s))
            if ''.join(map(str, scores[-len(sequence):])) == sequence:
                return len(scores) - len(sequence)
        i1 = (i1 + scores[i1] + 1) % len(scores)
        i2 = (i2 + scores[i2] + 1) % len(scores)
