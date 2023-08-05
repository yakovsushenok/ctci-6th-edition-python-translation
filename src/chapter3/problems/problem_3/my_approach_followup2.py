from typing import List


class EmptyStackException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "Empty Stack Exception"


class SetOfStacksFollowUp2:
    """
    Assumption here is that we can't have stacks that are not at full capacity, given they are not the last stack.
    So this means when we pop_at, we will shift the other elements of all stacks by 1.
    """

    def __init__(self, threshold: int) -> None:
        self.threshold = threshold
        self.current_stack: List[int] = []
        self.current_last_stack_num = 0
        self.stacks: List[List[int]] = [self.current_stack]

    def push(self, item: int) -> None:
        if len(self.current_stack) == self.threshold:
            new_stack = [item]
            self.stacks.append(new_stack)
            self.current_stack = new_stack
            self.current_last_stack_num += 1
        else:
            self.current_stack.append(item)

    def pop(self) -> int:
        if len(self.current_stack) == 0:
            raise EmptyStackException
        item = self.current_stack.pop()
        if len(self.current_stack) == 0 and len(self.stacks) != 1:
            self.current_stack = self.stacks[self.current_last_stack_num]
            self.stacks.pop()
            self.current_last_stack_num -= 1
            return item
        return item

    def pop_at(self, index: int) -> int:
        if index > self.current_last_stack_num:
            raise EmptyStackException
        if index == self.current_last_stack_num:
            return self.pop()
        else:
            stack_copy = self.stacks[index].copy()
            self.shift(index)
            return stack_copy.pop()

    def shift(self, index: int) -> None:
        for i in range(index, self.current_last_stack_num + 1):
            if i == index:
                self.stacks[i][-1] = self.stacks[i + 1][0]
                continue
            if i == self.current_last_stack_num:
                if len(self.stacks[i]) == 1:
                    self.stacks.pop()
                    self.current_last_stack_num -= 1
                else:
                    self.stacks[i][: len(self.stacks[i]) - 1] = self.stacks[i][1:]
                    self.stacks[i].pop()
                break

            self.stacks[i] = self.shift_one_stack(self.stacks[i], self.stacks[i + 1])

    def shift_one_stack(self, stack_prev, stack):
        stack_prev[: len(stack_prev) - 1] = stack_prev[1:]
        stack_prev[-1] = stack[0]
        return stack_prev

    def top(self) -> int:
        if len(self.current_stack) == 0:
            raise EmptyStackException
        return self.current_stack[-1]
