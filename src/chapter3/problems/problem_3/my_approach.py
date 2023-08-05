from typing import List
class EmptyStackException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "Empty Stack Exception"

class SetOfStack:
    def __init__(self, threshold: int) -> None:
        self.threshold = threshold
        self.current_stack: List[int] = []
        self.stacks: List[List[int]] = [self.current_stack]

    def push(self, item: int) -> None:
        if len(self.current_stack) > self.threshold:
            new_stack = [item]
            self.stacks.append(new_stack)
            self.current_stack = new_stack
        else: 
            self.current_stack.append(item)
    
    def pop(self) -> int:
        if self.current_stack == 0:
            raise EmptyStackException
        item = self.current_stack.pop()
        if len(self.current_stack) == 0:
            if len(self.stacks) == 1:
                return item
            else:
                self.current_stack = 