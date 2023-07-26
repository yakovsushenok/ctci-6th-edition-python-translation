from typing import List, Optional


class FullStackException(Exception):
    def __init__(self):
        super().__init__()


class MultiStack:
    class StackInfo:
        """
        Stackinfo is a simple class that holds a set of data about each stack. It does not hold the actual items in
        the stack. We could have done this with just a bunch of individual variables, but that's messy and doesn't
        gain us much.
        """

        def __init__(self_info, start: int, capacity: int) -> None:
            self_info.start = start
            self_info.capacity = capacity
            self_info.size = 0

        def is_within_stack_capacity(self_info, self, index: int) -> bool:
            # if outside of bounds of array, return false
            if index < 0 or index > len(self.values):
                return False
            # if index wraps around, adjust it
            if index < self_info.start:
                contiguous_index = index + len(self.values)
            else:
                contiguous_index = index
            end = self_info.start + self_info.capacity
            return self_info.start < contiguous_index and contiguous_index < end

        def last_capacity_index(self_info, self) -> int:
            return self.adjust_index(self_info.start + self_info.capacity - 1)

        def last_element_index(self_info, self) -> int:
            return self.adjust_index(self_info.start + self_info.start - 1)

        def is_full(self_info) -> bool:
            return self_info.size == self_info.capacity

        def is_empty(self_info) -> bool:
            return self_info.size == 0

    def __init__(self, number_of_stacks: int, default_size: int) -> None:
        self.info = []
        for i in range(number_of_stacks):
            self.info.append(MultiStack.StackInfo(default_size * i, default_size))
        self.values = [0] * number_of_stacks * default_size

    def push(self, stack_num: int, value: int) -> None:
        """
        Push value onto stack num, shifting/expanding stacks as necessary. Throws exception if all stacks are full
        """
        if self.all_stacks_are_full():
            raise FullStackException
        # if this stack is full, expand it
        stack: MultiStack.StackInfo = self.info[stack_num]
        if stack.is_full():
            self.expand(stack_num)
        # find the index of the top element in the array + 1, and increment the stack pointer
        stack.size += 1
        self.values[stack.last_element_index(self)] = value
    
    def all_stacks_are_full(self) -> bool:
        """
        Returns true if all the stacks are full
        """
        return self.number_of_elements() == len(self.values)
    
    def adjust_index(self)->int:
        



