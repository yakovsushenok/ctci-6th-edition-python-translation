from typing import List


class EmptyStackException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "Empty Stack Exception"


class SetOfStacksFollowUp:
    """
    TODO: should remove empty stacks
    """
    def __init__(self, threshold: int) -> None:
        self.threshold = threshold
        self.current_stack: List[int] = []
        self.current_stack_num = 0
        self.stacks: List[List[int]] = [self.current_stack]

    def push(self, item: int) -> None:
        if len(self.current_stack) == self.threshold:
            new_stack = [item]
            self.stacks.append(new_stack)
            self.current_stack = new_stack
            self.current_stack_num += 1
        else:
            self.current_stack.append(item)

    def pop(self) -> int:
        if len(self.current_stack) == 0:
            raise EmptyStackException
        item = self.current_stack.pop()
        if len(self.current_stack) == 0 and len(self.stacks) != 1:
            self.current_stack = self.stacks[self.current_stack_num]
            self.stacks.pop()
            self.current_stack_num -= 1
            return item
        return item

    def pop_at(self, index: int) -> int:
        if index > self.current_stack_num:
            raise EmptyStackException
        if index == self.current_stack_num:
            return self.pop()
        else:
            if len(self.stacks[index]) > 0:
                return self.stacks[index].pop()
            else:
                raise EmptyStackException

    def top(self) -> int:
        if len(self.current_stack) == 0:
            raise EmptyStackException
        return self.current_stack[-1]
