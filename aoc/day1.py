def solve1(text: str):
    return sum(map(int, text.split('\n')))


def solve2(text: str):
    numbers = list(map(int, text.split('\n')))
    result = 0
    seen = {result}
    index = 0
    while True:
        result += numbers[index]
        if result in seen:
            return result
        seen.add(result)
        index = (index + 1) % len(numbers)
