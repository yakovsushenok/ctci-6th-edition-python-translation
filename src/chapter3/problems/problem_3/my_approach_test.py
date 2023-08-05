import unittest
from my_approach import SetOfStacks, EmptyStackException


class StackMinTests(unittest.TestCase):
    def setUp(self) -> None:
        self.set_of_stacks = SetOfStacks(3)
        self.set_of_stacks.current_stack = [0, 1]

    def test_push(self):
        # When we call push and the current stack is not at threshold capacity
        item_to_be_pushed_1 = 2
        self.set_of_stacks.push(item_to_be_pushed_1)
        # it should push the item to the current stack
        self.assertEqual(self.set_of_stacks.current_stack[-1], item_to_be_pushed_1)
        # it should not increase the stack index
        self.assertEqual(self.set_of_stacks.current_stack_num, 0)
        self.assertEqual(len(self.set_of_stacks.stacks), 1)

        # When we call push and the current stack is at threshold capacity
        item_to_be_pushed_2 = 3
        self.set_of_stacks.push(item_to_be_pushed_2)
        # it should push the item to a newly created stack
        self.assertEqual(self.set_of_stacks.current_stack[-1], item_to_be_pushed_2)
        self.assertEqual(len(self.set_of_stacks.stacks), 2)
        self.assertEqual(self.set_of_stacks.current_stack_num, 1)

    def test_pop(self):
        # When we call pop and the current stack is NOT empty
        popped_item = self.set_of_stacks.pop()
        # and the number of stacks is 1, it should return the item that was popped
        self.assertEqual(popped_item, 1)

        # When we call pop and and the number of stacks is 1 and the current stack is empty
        self.set_of_stacks.pop()
        # it should raise an error
        self.assertRaises(EmptyStackException, lambda: self.set_of_stacks.pop())

        # When we call pop and there are more than 1 stack and the current stack is empty after popping
        self.set_of_stacks.push(0)
        self.set_of_stacks.push(1)
        self.set_of_stacks.push(2)
        self.set_of_stacks.push(3)  # here we push to the new stack
        previous_stacks_length = len(self.set_of_stacks.stacks)
        previous_stack_num = self.set_of_stacks.current_stack_num
        self.set_of_stacks.pop()
        # it should decrease the stacks size by 1
        self.assertEqual(len(self.set_of_stacks.stacks), previous_stacks_length - 1)
        self.assertEqual(self.set_of_stacks.current_stack_num, previous_stack_num - 1)

    def test_top(self):
        # When we call top
        # and current stack is NOT empty
        top = self.set_of_stacks.top()
        # it should return the item at the top of the stack
        self.assertEqual(top, 1)
        # and the current stack is empty
        self.set_of_stacks.pop()
        self.set_of_stacks.pop()
        # it should raise an exception
        self.assertRaises(EmptyStackException, lambda: self.set_of_stacks.top())


if __name__ == "__main__":
    unittest.main()
