import unittest
from ap_1_fixed_division import FixedMultiStack, FullStackException, EmptyStackException


class MyQueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixed_multi_stack = FixedMultiStack(4)

    def test_push(self):
        # When we call push, and the corresponding stack is not full, we expect the value to push to the
        # beginning of the stack
        stack_to_push_to = 1  # pushing to the second stack (since they start from 0)
        value_to_push = 34
        self.fixed_multi_stack.push(stack_to_push_to, value_to_push)
        expected_stack_values = [0, 0, 0, 0, 34, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.fixed_multi_stack.values, expected_stack_values)
        # and the size of the corresponding stack should increase by 1
        self.assertEqual(1, self.fixed_multi_stack.sizes[stack_to_push_to])
        # When we call push and the corresponding stack is full, we expect it to raise an exception
        self.fixed_multi_stack.push(stack_to_push_to, 2)
        self.fixed_multi_stack.push(stack_to_push_to, 3)
        self.fixed_multi_stack.push(stack_to_push_to, 4)
        self.assertRaises(
            FullStackException, lambda: self.fixed_multi_stack.push(stack_to_push_to, 5)
        )

    def test_pop(self):
        # When we call pop, and the corresponding stack is empty, we expect it to raise an exception
        self.assertRaises(EmptyStackException, lambda: self.fixed_multi_stack.pop(0))
        # When we call pop, and the corresponding stack is not empty, we should expect it to return
        # the value at the top of the stack
        value_to_be_popped = 12
        stack_to_pop_from = 0
        self.fixed_multi_stack.push(
            stack_to_pop_from, value_to_be_popped
        )  # first add a value to the stack
        self.assertEqual(
            value_to_be_popped, self.fixed_multi_stack.pop(stack_to_pop_from)
        )
        # and the size of the corresponding stack should decrease by 1
        self.assertEqual(0, self.fixed_multi_stack.sizes[stack_to_pop_from])
        # and the value should have been deleted from the stack
        expected_stack_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(expected_stack_values, self.fixed_multi_stack.values)

    def test_peak(self):
        # When we call peek, and the stack is empty, it should raise an exception
        self.assertRaises(EmptyStackException, lambda: self.fixed_multi_stack.peek(0))
        # When we call peek, and the stack is not empty, it should return the value at the top of the
        # corresponding stack
        self.fixed_multi_stack.push(0, 1)
        self.fixed_multi_stack.push(0, 2)
        self.assertEqual(self.fixed_multi_stack.peek(0), 2)


if __name__ == "__main__":
    unittest.main()
