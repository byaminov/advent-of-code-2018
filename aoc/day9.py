from collections import defaultdict


def solve1(n_players=479, last_marble_worth=7103500):
    current = Node(0)
    current.right = current
    current.left = current

    scores = defaultdict(int)
    current_player = 1
    for m in range(1, last_marble_worth + 1):
        if m % 23 != 0:
            first = current.right
            new_marble = Node(m)
            first.insert_right(new_marble)
            current = first.right
        else:
            scores[current_player] += m

            to_remove = current
            for i in range(7):
                to_remove = to_remove.left

            scores[current_player] += to_remove.marble

            current = to_remove.right
            to_remove.remove_self()

        current_player = (current_player + 1) % n_players

    return max(scores.values())


class Node:
    def __init__(self, marble):
        self.marble = marble
        self.left = None
        self.right = None

    def insert_right(self, node):
        current_right = self.right
        self.right = node
        node.right = current_right
        current_right.left = node
        node.left = self

    def remove_self(self):
        left = self.left
        right = self.right
        left.right = right
        right.left = left

    def __str__(self):
        return f'Node({self.marble})'
