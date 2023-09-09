import unittest
from src.chapter3.problems.problem_5.my_approach import SortStack


class SortStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sort_stack = SortStack()

    def test_push(self):
        # When we call push, and the stack is empty, the item should be pushed to the main stack
        item_to_push = 3
        self.sort_stack.push(item_to_push)
        self.assertEqual(self.sort_stack.main_stack.peek(), item_to_push)
        # When we call push, and the stack is not empty,
        # and the item being pushed is smaller than the current top item,
        item_to_push_1 = 1
        self.sort_stack.push(item_to_push_1)
        # then the item being pushed should be pushed to the top of the stack
        self.assertEqual(self.sort_stack.main_stack.top.data, item_to_push_1)
        # and the item being pushed is greater than the top of the stack
        # but smaller than the bottom of the stack,
        item_to_push_2 = 2
        self.sort_stack.push(item_to_push_2)
        # then the item being pushed should be pushed to the middle of the stack
        self.assertEqual(self.sort_stack.main_stack.top.data, item_to_push_1)
        self.assertEqual(self.sort_stack.main_stack.top.next.data, item_to_push_2)
        # and the item being pushed is greater than all elements in the stack
        item_to_push_3 = 4
        self.sort_stack.push(item_to_push_3)
        # then the item being pushed should be pushed to the bottom of the stack
        self.assertEqual(
            self.sort_stack.main_stack.top.next.next.next.data, item_to_push_3
        )


if __name__ == "__main__":
    unittest.main()
