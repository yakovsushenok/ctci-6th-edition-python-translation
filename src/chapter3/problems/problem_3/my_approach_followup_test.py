import unittest
from my_approach_followup import SetOfStacksFollowUp, EmptyStackException


class SetOfStacksFollowUpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.set_of_stacks = SetOfStacksFollowUp(2)
        self.set_of_stacks.current_stack = [0, 1]
        self.set_of_stacks.push(2)  # 2nd sub-stack
        self.set_of_stacks.push(3)
        self.set_of_stacks.push(4)  # 3rd sub-stack

    def test_pop_at(self):
        # When we call pop_at,
        # and the stack that is being popped at exists,
        # and it is not empty, then it should return the item being popped
        item_popped = self.set_of_stacks.pop_at(1)
        self.assertEqual(item_popped, 3)
        # and the the stack is empty, then it should raise an exception
        self.set_of_stacks.pop_at(1)
        self.assertRaises(EmptyStackException, lambda: self.set_of_stacks.pop_at(1))

        # and the stack that is being popped does not exist
        # it should raise an exception
        self.assertRaises(EmptyStackException, lambda: self.set_of_stacks.pop_at(3))


if __name__ == "__main__":
    unittest.main()
