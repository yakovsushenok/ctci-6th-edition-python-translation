import unittest
from my_stack import MyStack, StackNode, EmptyStackException


class MyStackTests(unittest.TestCase):
    def setUp(self) -> None:
        node1 = StackNode(1)  # type: ignore
        node2 = StackNode(2)  # type: ignore
        node3 = StackNode(3)  # type: ignore
        node3.next = node2
        node2.next = node1
        node1.next = None
        self.my_stack = MyStack(node3)
        self.empty_stack = MyStack(None)

    def test_pop(self):
        result_node_data = self.my_stack.pop()
        # When calling pop, it should return the item that was popped, equal
        # to the data the top node has
        self.assertEqual(result_node_data, 3)
        # When calling pop, it should set the top node to the next node in the
        # stack
        self.assertEqual(self.my_stack.top.data, 2)
        # When all elements are removed, calling pop should raise an exception
        self.assertRaises(EmptyStackException, lambda: self.empty_stack.pop())

    def test_push(self):
        self.my_stack.push(4)
        # When calling push, the top node should have data equal to the item
        # pushed,
        self.assertEqual(self.my_stack.top.data, 4)
        # and it should set the next node of the top node equal to the the
        # previous top node
        self.assertEqual(self.my_stack.top.next.data, 3)

    def test_peek(self):
        result_node_data = self.my_stack.peek()
        # When caling peek, it should return the data of the top node
        self.assertEqual(result_node_data, 3)
        # When calling peek and there are no nodes in the stack, it should
        # raise an exception
        self.assertRaises(EmptyStackException, lambda: self.empty_stack.peek())

    def test_is_empty(self):
        self.assertFalse(self.my_stack.is_empty())
        self.assertTrue(self.empty_stack.is_empty())


if __name__ == "__main__":
    unittest.main()
