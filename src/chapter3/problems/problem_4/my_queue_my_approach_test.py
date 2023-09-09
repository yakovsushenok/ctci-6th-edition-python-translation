import unittest
from src.chapter3.problems.problem_4.my_queue_my_approach import MyQueueViaStacks
from src.chapter3.my_stack import EmptyStackException


class MyQueueViaStacksTests(unittest.TestCase):
    def setUp(self) -> None:
        self.my_queue_via_stacks = MyQueueViaStacks()

    def test_add(self):
        # When we call add, we expect the left stack to have populated with an element
        item_to_add = 123
        self.my_queue_via_stacks.add(item_to_add)
        self.assertEqual(self.my_queue_via_stacks.left_stack.peek(), item_to_add)

    def test_remove(self):
        # When we call remove, and the left stack is NOT empty,
        first_item_added_to_queue = 0
        self.my_queue_via_stacks.add(first_item_added_to_queue)
        self.my_queue_via_stacks.add(1)
        self.my_queue_via_stacks.add(2)
        # and the right stack is empty, it should carry over all of the elements from the left stack to the right, and
        # the it should remove the first item added to the queue
        item_popped = self.my_queue_via_stacks.remove()
        self.assertEqual(first_item_added_to_queue, item_popped)
        self.assertEqual(self.my_queue_via_stacks.right_stack.peek(), 1)

        # When we call remove, and the left stack is empty, it should not carry over the items in the left stack
        # and it should return the top item from the right stack
        item_popped_2 = self.my_queue_via_stacks.remove()
        self.assertEqual(item_popped_2, 1)
        self.assertRaises(
            EmptyStackException, lambda: self.my_queue_via_stacks.left_stack.peek()
        )

        # When we call remove, and the left stack is NOT empty, and the right stack is not empty,
        # it should not carry over any new items from the left stack
        self.my_queue_via_stacks.add(3)
        item_popped_3 = self.my_queue_via_stacks.remove()
        self.assertEqual(item_popped_3, 2)
        self.assertEqual(self.my_queue_via_stacks.left_stack.peek(), 3)

        # When we call remove, and the left stack is empty, and the right stack is empty, it should raise an exception
        self.my_queue_via_stacks.remove()
        self.assertRaises(
            EmptyStackException, lambda: self.my_queue_via_stacks.remove()
        )

    def test_peek(self):
        # When we call peek, and the left stack is not empty, and the right stack is empty
        first_item_to_add = 0
        self.my_queue_via_stacks.add(first_item_to_add)
        self.my_queue_via_stacks.add(1)
        # it should return the first item to be added
        self.assertEqual(self.my_queue_via_stacks.peek(), first_item_to_add)

        # When we call peek, and both stacks are empty, it should raise an exception
        self.my_queue_via_stacks.remove()
        self.my_queue_via_stacks.remove()
        self.assertRaises(EmptyStackException, lambda: self.my_queue_via_stacks.peek())


if __name__ == "__main__":
    unittest.main()
