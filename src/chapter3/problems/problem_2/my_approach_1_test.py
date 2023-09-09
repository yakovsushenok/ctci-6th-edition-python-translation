import unittest
from src.chapter3.problems.problem_2.my_approach_1 import StackMin, EmptyStackException


class StackMinTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_stack = StackMin()
        self.my_stack.push(5)
        self.my_stack.push(3)
        self.my_stack.push(6)

    def test_push(self):
        # When we push to a stack
        # and the value pushed is greater than the minimum
        self.my_stack.push(10)
        # then the minimum is not changed
        self.assertEqual(self.my_stack.min, 3)
        # and the top value of the stack is the value pushed
        self.assertEqual(self.my_stack.top(), 10)
        # When we push to a stack and the value pushed is smaller than the minimum
        self.my_stack.push(2)
        # then the minimum should have changed to the value that has been just pushed
        self.assertEqual(self.my_stack.min, 2)
        # and we push a second value that is the same value as the current minimum one,
        self.my_stack.push(2)
        # then the min_stack should have 2 values of the minimum value inside
        self.assertEqual(self.my_stack.min_stack, [5, 3, 2, 2])

    def test_pop(self):
        min_stack_before = self.my_stack.min_stack.copy()
        length_of_stack_before = len(self.my_stack.stack)
        # When we call pop on a stack that is NOT empty
        self.my_stack.pop()
        # and the value popped is not the minimum, we should expect the min_stack to have stayed the same
        self.assertEqual(self.my_stack.min_stack, min_stack_before)
        # we should expect the length of the stack to have decreased by 1
        self.assertEqual(length_of_stack_before - 1, len(self.my_stack.stack))
        # When we call pop on a stack that is NOT empty
        self.my_stack.pop()
        # and the value popped is the current minimum, we should expect the min_stack to have decreased
        self.assertEqual(len(min_stack_before) - 1, len(self.my_stack.min_stack))
        # When we call pop on a stack that is empty
        self.my_stack.pop()
        # we should expect an exception to be raised
        self.assertRaises(EmptyStackException, lambda: self.my_stack.pop())
        # we should expect the min_stack to be empty
        self.assertEqual(len(self.my_stack.min_stack), 0)

    def test_get_min(self):
        # When the stack is NOT empty, and we call get_min, it should return the minimum element in the stack
        self.assertEqual(self.my_stack.get_min(), 3)
        # When the stack is empty
        self.my_stack.pop()
        self.my_stack.pop()
        self.my_stack.pop()
        # and we call ge_min, it should raise an error
        self.assertRaises(EmptyStackException, lambda: self.my_stack.get_min())

    def test_top(self):
        # When the stack is NOT empty, and we call top, it should return the top element of the stack
        self.assertEqual(self.my_stack.top(), 6)
        # When the stack is empty
        self.my_stack.pop()
        self.my_stack.pop()
        self.my_stack.pop()
        # and we call top, it should raise an error
        self.assertRaises(EmptyStackException, lambda: self.my_stack.top())


if __name__ == "__main__":
    unittest.main()
