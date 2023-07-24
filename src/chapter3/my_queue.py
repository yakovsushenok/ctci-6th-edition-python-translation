from typing import Type, Any, Optional


class NoSuchElementException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "No Such Element Exception"


class QueueNode:
    def __init__(self, data: Type[Any]) -> None:
        self.data = data
        self.next: Optional[QueueNode] = None


class MyQueue:
    def __init__(
        self,
        first_node: Optional[QueueNode] = None,
        last_node: Optional[QueueNode] = None,
    ) -> None:
        self.first_node = first_node
        self.last_node = last_node

    def add(self, item: Type[Any]) -> None:
        t = QueueNode(item)
        if self.last_node is not None:
            self.last_node.next = t
        self.last_node = t

        if self.first_node is None:
            self.first_node = self.last_node

    def remove(self) -> Type[Any]:
        if self.first_node is None:
            raise NoSuchElementException
        data = self.first_node.data
        self.first_node = self.first_node.next
        if self.first_node is None:
            self.last_node = None
        return data

    def peek(self) -> Type[Any]:
        if self.first_node is None:
            raise NoSuchElementException
        return self.first_node.data

    def is_empty(self) -> bool:
        return self.first_node is None
