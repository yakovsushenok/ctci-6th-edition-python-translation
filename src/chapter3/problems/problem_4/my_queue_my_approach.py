from typing import Any, Type
from src.chapter3.my_stack import MyStack, EmptyStackException


class MyQueueViaStacks:
    """
    Idea is that we have a left stack, to which we push to, and a right stack, to which we push from the left stack
    and also remove when we call remove from the queue
    """

    def __init__(self) -> None:
        self.left_stack = MyStack()
        self.right_stack = MyStack()

    def add(self, data: Type[Any]) -> None:
        self.left_stack.push(data)

    def remove(self) -> Type[Any]:
        if self.right_stack.is_empty():
            if self.left_stack.is_empty():
                raise EmptyStackException
            self.carry_over()
        return self.right_stack.pop()

    def peek(self) -> Type[Any]:
        if self.right_stack.is_empty():
            if self.left_stack.is_empty():
                raise EmptyStackException
            self.carry_over()
        return self.right_stack.peek()

    def carry_over(self) -> None:
        """
        Carries over all elements from left stack to right. Assumption is that the right stack is empty when we do this.
        """
        while not self.left_stack.is_empty():
            popped_left_stack_item = self.left_stack.pop()
            self.right_stack.push(popped_left_stack_item)
