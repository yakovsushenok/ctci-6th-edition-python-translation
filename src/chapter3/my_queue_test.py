import unittest
from src.chapter3.my_queue import MyQueue, QueueNode, NoSuchElementException


class MyQueueTests(unittest.TestCase):
    def setUp(self) -> None:
        node1 = QueueNode(1)  # type: ignore
        node2 = QueueNode(2)  # type: ignore
        node3 = QueueNode(3)  # type: ignore
        node1.next = node2
        node2.next = node3
        self.my_queue = MyQueue(node1, node3)
        self.empty_queue = MyQueue()

    def test_add(self):
        item_to_add = 4
        previous_last_node = self.my_queue.last_node
        # When we call add and last_node is not None, we expect the last_node to have data equal to the item added
        self.my_queue.add(item_to_add)
        self.assertEqual(self.my_queue.last_node.data, item_to_add)
        # and the previous last_node to have the next node as the current last_node
        self.assertEqual(previous_last_node.next.data, item_to_add)

        # When we call add and last_node is None, we expect the last_node's data to equal to the item that
        # just got pushed
        self.empty_queue.add(item_to_add)
        self.assertEqual(self.empty_queue.last_node.data, item_to_add)
        # and the first_node's to equal to the item that just got pushed
        self.assertEqual(self.empty_queue.first_node.data, item_to_add)

    def test_remove(self):
        # When we call remove and the queue is empty, we expect it
        # to throw an exception
        self.assertRaises(NoSuchElementException, lambda: self.empty_queue.remove())

        # When we call remove and the queue is not empty and has more than one
        # element, it should return the data of the first node
        data_removed = self.my_queue.remove()
        self.assertEqual(data_removed, 1)
        # and the first_node data should equal to the previous second node's data
        self.assertEqual(self.my_queue.first_node.data, 2)

        # When we remove the only node that's left, we should set the last node to none
        self.my_queue.remove()
        self.my_queue.remove()
        self.assertEqual(self.my_queue.first_node, None)
        self.assertEqual(self.my_queue.last_node, None)

    def test_peek(self):
        # When we call peek and the queue is empty, we expect it to raise an exception
        self.assertRaises(NoSuchElementException, lambda: self.empty_queue.peek())
        # When we call peek and the queue is not empty, we expect it to return the first_node's data
        self.assertEqual(self.my_queue.peek(), 1)

    def test_is_empty(self):
        # When we call is_empty on an empty queue, we expect it to return True
        self.assertTrue(self.empty_queue.is_empty())
        # When we call is_empty on queue that is not empty, we expect it to return False
        self.assertFalse(self.my_queue.is_empty())


if __name__ == "__main__":
    unittest.main()
