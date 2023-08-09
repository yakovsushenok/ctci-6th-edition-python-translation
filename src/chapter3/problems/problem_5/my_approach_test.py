import unittest
from src.chapter3.problems.problem_5.my_approach import SortStack


class SortStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sort_stack = SortStack()

    def test_push(self):
        # When we call push, and the stack is empty, the item should be pushed to the main stack
        item_to_push = 2
        self.sort_stack.push(item_to_push)
        self.assertEqual(self.sort_stack.main_stack.peek(), item_to_push)


if __name__ == "__main__":
    unittest.main()
