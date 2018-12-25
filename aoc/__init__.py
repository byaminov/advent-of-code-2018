import matplotlib.pyplot as plt
import networkx as nx


def search_minimum_matching(predicate, start_from: int) -> int:
    if predicate(start_from):
        return start_from
    increment = 1
    while not predicate(start_from + increment):
        increment *= 2
    return search_minimum_matching(predicate, start_from + increment // 2 + 1)


def draw_graph(tree, file_name='graph.png'):
    f = plt.figure()
    subplot = f.add_subplot(111)
    nx.draw(tree, ax=subplot)
    layout = nx.spring_layout(tree)
    nx.draw_networkx_nodes(tree, pos=layout, ax=subplot)
    nx.draw_networkx_edges(tree, pos=layout, ax=subplot)
    nx.draw_networkx_labels(tree, pos=layout, ax=subplot)
    f.savefig(file_name)
