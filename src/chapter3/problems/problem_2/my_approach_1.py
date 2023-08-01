from typing import List


class EmptyStackException(Exception):
    def __init__(self):
        super().__init__()
        self.message = "Empty Stack Exception"


class StackMin:
    def __init__(self) -> None:
        self.stack: List[int] = []
        self.min_stack: List[int] = []
        self.min = float("inf")

    def push(self, value: int) -> None:
        if value <= self.min:
            self.min_stack.append(value)
            self.min = value
        self.stack.append(value)

    def pop(self) -> None:
        if len(self.stack) > 0:
            if self.stack[-1] == self.min:
                self.min_stack.pop()
                if len(self.min_stack) > 0:
                    self.min = self.min_stack[-1]
                else:
                    self.min = float("inf")
            self.stack.pop()
        else:
            raise EmptyStackException

    def get_min(self) -> int:
        if len(self.stack) > 0:
            return self.min  # type: ignore
        else:
            raise EmptyStackException

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            raise EmptyStackException
