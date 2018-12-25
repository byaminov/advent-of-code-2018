from typing import NamedTuple


def parse_tree(text):
    numbers = list()
    for number_ in text.split(' '):
        if not number_.strip():
            continue
        numbers.append(int(number_))
    numbers = iter(numbers)

    def parse_node():
        node = Node(children=[], meta=[])
        n_children, n_meta = next(numbers), next(numbers)
        for i in range(n_children):
            node.children.append(parse_node())
        for i in range(n_meta):
            node.meta.append(next(numbers))
        return node

    return parse_node()


def solve1(text: str):
    root = parse_tree(text)

    def sum_meta(node):
        return sum(node.meta) + sum(map(lambda c: sum_meta(c), node.children))

    return sum_meta(root)


def solve2(text: str):
    root = parse_tree(text)

    def value(node: Node):
        if not node.children:
            return sum(node.meta)
        children_values = 0
        for m in node.meta:
            i = m - 1
            if i < 0 or i >= len(node.children):
                continue
            children_values += value(node.children[i])
        return children_values

    return value(root)


class Node(NamedTuple):
    children: list
    meta: list
