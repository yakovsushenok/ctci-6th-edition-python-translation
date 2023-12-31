import unittest
from src.chapter3.problems.problem_1.ap_2_flexible_divisions import (
    MultiStack,
    FullStackException,
    EmptyStackException,
)


class MultiStackTest(unittest.TestCase):
    def setUp(self) -> None:
        self.multi_stack = MultiStack(number_of_stacks=3, default_size=4)
        self.multi_stack_small = MultiStack(number_of_stacks=2, default_size=2)
        self.multi_stack_small2 = MultiStack(number_of_stacks=3, default_size=2)

    def test_set_up(self):
        # When we call __init__, we should create a list of StackInfo objects
        self.assertEqual(len(self.multi_stack.info), 3)
        self.assertEqual(self.multi_stack.info[0].start, 0)
        self.assertEqual(self.multi_stack.info[1].start, 4)
        self.assertEqual(self.multi_stack.info[2].start, 8)
        # and values list
        expected_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.multi_stack.values, expected_values)

    def test_push(self):
        # When we call push, and the multi stack is not full, and the stack we want to push to is not full
        value_to_push_1 = 123
        self.multi_stack_small.push(1, value_to_push_1)
        # the corresponding stack's size should increase by 1
        self.assertEqual(self.multi_stack_small.info[1].size, 1)
        # and the top element of the stack should be equal to the value that we pushed
        self.assertEqual(self.multi_stack_small.values, [0, 0, value_to_push_1, 0])
        # When we call push the second time on the same stack, it should push to to the top of the stack,
        # consequently pushing to the index after the firstly pushed value
        value_to_push_2 = 456
        self.multi_stack_small.push(1, value_to_push_2)
        self.assertEqual(
            self.multi_stack_small.values, [0, 0, value_to_push_1, value_to_push_2]
        )
        # When we call push and the corresponding stack is full, it should be expanded
        value_to_push_3 = 789
        self.multi_stack_small.push(1, value_to_push_3)
        self.assertEqual(
            self.multi_stack_small.values,
            [value_to_push_3, 0, value_to_push_1, value_to_push_2],
        )
        # When we call push and all stack are full, it should raise an exception
        self.multi_stack_small.push(1, 963)
        self.assertRaises(
            FullStackException, lambda: self.multi_stack_small.push(1, 852)
        )
        # When we call push on a particular stack that it at full capacity and
        # the next stack is at capacity too, the stack being pushed to should be
        # expanded and the next stack should move by one place
        self.multi_stack_small2.push(1, 123)
        self.multi_stack_small2.push(1, 456)
        self.multi_stack_small2.push(0, 789)
        self.multi_stack_small2.push(0, 963)
        self.multi_stack_small2.push(0, 852)
        self.assertEqual(self.multi_stack_small2.values, [789, 963, 852, 123, 456, 0])

    def test_pop(self):
        # When we call pop and the stack is empty, it should raise an exception
        self.assertRaises(EmptyStackException, lambda: self.multi_stack_small.pop(0))
        # When we call pop and the stack is NOT empty,
        value_to_be_popped = 123
        self.multi_stack_small.push(0, value_to_be_popped)
        result_value = self.multi_stack_small.pop(0)
        # it should return the value that is popped
        self.assertEqual(result_value, value_to_be_popped)
        # it should decrease the size of the stack by 1
        self.assertEqual(self.multi_stack_small.info[0].size, 0)


if __name__ == "__main__":
    unittest.main()
