from src.chapter4.graph import Node
from src.chapter3.my_queue import MyQueue
from collections import defaultdict


def path_exists_bfs(node_1: Node, node_2: Node) -> bool:
    marked_nodes: dict[Node, bool] = defaultdict()
    queue = MyQueue()
    marked_nodes[node_1] = True

    queue.add(node_1)

    while not queue.is_empty():
        r = queue.remove()
        if r.children is None:
            continue
        for node in r.children:
            if node == node_2:
                return True
            if not marked_nodes.get(node, False):
                marked_nodes[node] = True
                queue.add(node)
    return False
