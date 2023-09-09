import unittest
from src.chapter3.problems.problem_3.my_approach_followup import SetOfStacksFollowUp


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
        # and the stack has 1 remaining element, then after popping, that stack should be removed and the
        # last stack index should decrease by 1
        current_last_stack_num_before_popping = (
            self.set_of_stacks.current_last_stack_num
        )
        self.set_of_stacks.pop_at(1)
        self.assertEqual(
            self.set_of_stacks.current_last_stack_num,
            current_last_stack_num_before_popping - 1,
        )
        self.assertEqual(self.set_of_stacks.stacks[1], [4])


if __name__ == "__main__":
    unittest.main()
