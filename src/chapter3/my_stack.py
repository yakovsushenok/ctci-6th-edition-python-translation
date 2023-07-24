from typing import Type, Any, Optional


class EmptyStackException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "Empty Stack Exception"


class StackNode:
    def __init__(self, data: Type[Any]) -> None:
        self.data = data
        self.next: Optional[StackNode] = None


class MyStack:
    def __init__(self, top: Optional[StackNode] = None) -> None:
        self.top = top

    def pop(self) -> Type[Any]:
        if self.top is None:
            raise EmptyStackException
        item = self.top.data
        self.top = self.top.next
        return item

    def push(self, item: Type[Any]):
        t = StackNode(item)
        t.next = self.top
        self.top = t

    def peek(self) -> Type[Any]:
        if self.top is None:
            raise EmptyStackException
        return self.top.data

    def is_empty(self) -> bool:
        return self.top is None
