import networkx as nx


def solve1(text: str):
    g = nx.Graph()

    for line in text.split('\n'):
        node = tuple(map(int, line.split(',')))
        g.add_node(node)
        for other in g.nodes:
            if dist(other, node) <= 3:
                g.add_edge(other, node)

    return len(list(nx.connected_components(g)))


def dist(x, y):
    return abs(x[0] - y[0]) + \
           abs(x[1] - y[1]) + \
           abs(x[2] - y[2]) + \
           abs(x[3] - y[3])
