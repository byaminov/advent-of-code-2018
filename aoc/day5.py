def solve1(text: str, exclude=None):
    chars = list()

    for c in text:
        if c.lower() == exclude:
            continue
        if chars and chars[-1] != c and chars[-1].lower() == c.lower():
            chars.pop()
        else:
            chars.append(c)

    return len(chars)


def solve2(text: str):
    return min(solve1(text, excluded)
               for excluded in set(text.lower()))
