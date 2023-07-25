from typing import List


class FullStackException(Exception):
    def __init__(self):
        super().__init__()


class FixedMultiStack:
    def __init__(self, stack_size: int) -> None:
        self.number_of_stacks = 3
        self.stack_capacity = stack_size
        self.values: List[int] = [0] * self.number_of_stacks * stack_size
        self.sizes: List[int] = [0] * self.number_of_stacks

    def push(self, stack_num: int, value: int) -> None:
        if self.is_full(stack_num):
            raise FullStackException
        self.sizes[stack_num] += 1
        self.values[self.index_of_top(stack_num)] = value

    def is_full(self, stack_num: int) -> bool:
        return self.sizes[stack_num] == self.stack_capacity

    def index_of_top(self, stack_num: int) -> int:
        offset = stack_num * self.stack_capacity
        size = self.sizes[stack_num]
        return offset + size - 1
