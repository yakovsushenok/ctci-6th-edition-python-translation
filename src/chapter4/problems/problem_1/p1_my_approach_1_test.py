import unittest
from src.chapter4.graph import Node
from src.chapter4.problems.problem_1.my_approach_1 import path_exists_bfs


class MyStackTests(unittest.TestCase):
    def setUp(self) -> None:
        self.node_01 = Node(0)
        self.node_11 = Node(1)
        self.node_21 = Node(2)
        self.node_31 = Node(3)
        self.node_41 = Node(4)
        self.node_51 = Node(5)
        self.node_01.children = [self.node_21]
        self.node_11.children = [self.node_21, self.node_31]
        self.node_21.children = [self.node_41]
        self.node_31.children = [self.node_51]
        self.node_41.children = [self.node_11]

        self.node_02 = Node(0)
        self.node_12 = Node(1)
        self.node_22 = Node(2)
        self.node_32 = Node(3)
        self.node_42 = Node(4)
        self.node_52 = Node(5)
        self.node_02.children = [self.node_12]
        self.node_12.children = [self.node_22, self.node_32]
        self.node_22.children = [self.node_42]
        self.node_42.children = [self.node_52]

        self.node_03 = Node(0)
        self.node_13 = Node(1)
        self.node_23 = Node(2)
        self.node_33 = Node(3)
        self.node_43 = Node(4)
        self.node_53 = Node(5)
        self.node_03.children = [self.node_13, self.node_23]
        self.node_13.children = [self.node_33]
        self.node_33.children = [self.node_43]
        self.node_43.children = [self.node_23]

    def test_1_path_exists_bfs(self):
        # Paths exist
        path_exists = path_exists_bfs(self.node_01, self.node_51)
        self.assertEqual(path_exists, True)
        path_exists = path_exists_bfs(self.node_02, self.node_52)
        self.assertEqual(path_exists, True)
        # Path doesn't exist
        path_exists = path_exists_bfs(self.node_03, self.node_53)
        self.assertEqual(path_exists, False)


if __name__ == "__main__":
    unittest.main()
