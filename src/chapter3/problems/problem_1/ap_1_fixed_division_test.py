import unittest
from ap_1_fixed_division import FixedMultiStack


class MyQueueTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixed_multi_stack = FixedMultiStack(4)

    def test_push(self):
        # When we call push, and the corresponding stack is not full, 
        self.fixed_multi_stack.push(2)


if __name__ == "__main__":
    unittest.main()
