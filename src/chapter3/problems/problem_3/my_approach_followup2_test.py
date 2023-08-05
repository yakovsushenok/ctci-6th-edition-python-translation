import unittest
from my_approach_followup2 import SetOfStacksFollowUp2


class SetOfStacksBookFollowUpTests(unittest.TestCase):
    def setUp(self) -> None:
        self.set_of_stacks = SetOfStacksFollowUp2(2)
        self.set_of_stacks.current_stack = [0, 1]
        self.set_of_stacks.stacks[0] = self.set_of_stacks.current_stack
        self.set_of_stacks.push(2)  # 2nd sub-stack
        self.set_of_stacks.push(3)
        self.set_of_stacks.push(4)  # 3rd sub-stack
        self.set_of_stacks.push(5)

    def test_pop_at(self):
        # When we call pop_at and the last stack has more than 1 element
        # it should shift all elements that are to the right of the popped element by 1, to the left
        # currently, before popping, the stacks are:
        # stack_1 = [0,1], stack_2 = [2,3], stack_3 = [4,5]
        expected_stack_0_after_popping = [0, 1]
        expected_stack_1_after_popping = [2, 4]
        expected_stack_2_after_popping = [5]
        popped_item = self.set_of_stacks.pop_at(1)
        self.assertEqual(popped_item, 3)
        self.assertEqual(expected_stack_0_after_popping, self.set_of_stacks.stacks[0])
        self.assertEqual(expected_stack_1_after_popping, self.set_of_stacks.stacks[1])
        self.assertEqual(expected_stack_2_after_popping, self.set_of_stacks.stacks[2])

        # When we call pop_at and the last stack has one element
        # it should shift all elements that are to the right of the popped element by 1, to the left
        # and it should delete the last stack
        # currently, before popping, the stacks are:
        # stack_1 = [0,1], stack_2 = [2,4], stack_3 = [5]
        expected_stack_0_after_popping = [0, 1]
        expected_stack_1_after_popping = [2, 5]
        popped_item = self.set_of_stacks.pop_at(1)
        self.assertEqual(popped_item, 4)
        self.assertEqual(expected_stack_0_after_popping, self.set_of_stacks.stacks[0])
        self.assertEqual(expected_stack_1_after_popping, self.set_of_stacks.stacks[1])
        self.assertEqual(len(self.set_of_stacks.stacks), 2)
        self.assertEqual(self.set_of_stacks.current_last_stack_num, 1)


if __name__ == "__main__":
    unittest.main()
