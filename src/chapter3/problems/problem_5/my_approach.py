from typing import Any, Type
from src.chapter3.my_stack import MyStack


class SortStack:
    def __init__(self) -> None:
        self.main_stack = MyStack()
        self.temp_stack = MyStack()

    def push(self, item: Type[Any]) -> None:
        if self.is_empty() or item <= self.main_stack.peek():
            self.main_stack.push(item)
        else:
            while not self.main_stack.is_empty() and item > self.main_stack.peek():
                popped_from_main_stack = self.main_stack.pop()
                self.temp_stack.push(popped_from_main_stack)
            while not self.temp_stack.is_empty():
                popped_from_temp_stack = self.temp_stack.pop()
                self.main_stack.push(popped_from_temp_stack)

    def pop(self) -> Type[Any]:
        return self.main_stack.pop()

    def is_empty(self) -> bool:
        return self.main_stack.is_empty()
