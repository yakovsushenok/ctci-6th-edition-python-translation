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
            """
            Check if an index on the full array is within the stack boundaries. The
            stack can wrap around to the start of the array.
            """
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
            return self.adjust_index(self_info.start + self_info.size - 1)

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

    def shift(self, stack_num: int) -> None:
        """
        Shift items in stack over by one element. If we have available capacity, then
        we'll end up shrinking the stack by one element. If we don't have available
        capacity, then we'll need to shift the next stack over too. */
        """
        print(f"/// Shifting stack {stack_num}")
        stack: MultiStack.StackInfo = self.info[stack_num]
        # If this stack is at its full capacity, then you need to move the next stack over by one element.
        # This stack can now claim the freed index
        if stack.size >= stack.capacity:
            next_stack = (stack_num + 1) % len(self.info)
            self.shift(next_stack)
        # Shift all elements in stack over by one
        index = stack.last_capacity_index(self)
        while stack.is_within_stack_capacity(self, index):
            self.values[index] = self.values[self.previous_index(index)]
            index = self.previous_index(index)
        # Adjust stack data
        self.values[stack.start] = 0  # clear item
        stack.start = self.next_index(stack.start)  # move start
        stack.capacity -= 1

    def next_index(self, index: int) -> int:
        return self.adjust_index(index + 1)

    def previous_index(self, index: int) -> int:
        """
        Get index before this index, adjusted for wrap around
        """
        return self.adjust_index(index - 1)

    def all_stacks_are_full(self) -> bool:
        """
        Returns true if all the stacks are full
        """
        return self.number_of_elements() == len(self.values)

    def adjust_index(self, index: int) -> int:
        """
        adjust index to be within the range of 0 -> length - 1.
        """
        max = len(self.values)
        return index % max

    def expand(self, stack_num: int) -> None:
        """
        Expand stack by shifting over other stacks
        """
        self.shift((stack_num + 1) % len(self.info))
        self.info[stack_num].capacity += 1

    def number_of_elements(self):
        size = 0
        for sd in self.info:
            size += sd.size
        return size
