from typing import List, Optional


class Node:
    children: Optional[List["Node"]] = None

    def __init__(self, value: int) -> None:
        self.value = value


class Graph:
    nodes: List[Node]
