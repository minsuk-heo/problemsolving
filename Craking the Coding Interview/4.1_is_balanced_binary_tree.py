import unittest
import math

__author__ = 'Minsuk Heo'

"""
Binary Tree

check if the Binary tree is balanced
"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.head = Node(None)

        #test purpose lists
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    def traverse(self, cur):
        if cur is None:
            return True
        if cur.left is not None:
            lDepth = self.getHeight(cur.left)
        else:
            lDepth = 0
        if cur.right is not None:
            rDepth = self.getHeight(cur.right)
        else:
            rDepth = 0

        heightDiff = math.fabs(lDepth - rDepth)
        if heightDiff > 1:
            return False

        else:
            return self.traverse(cur.left) and self.traverse(cur.right)

    def getHeight(self, node):
        if node is None:
            return 0
        return max(self.getHeight(node.left), self.getHeight(node.right))+1

    def is_balanced(self):
        if self.checkHeight(self.head) == -1:
            return False
        else:
            return True

    def checkHeight(self, node):
        if node is None:
            return 0

        # if left subtree is balanced
        leftHeight = self.checkHeight(node.left)
        if leftHeight == -1:
            return -1
        # if right subtree is balanced
        rightHeight = self.checkHeight(node.right)
        if rightHeight == -1:
            return -1

        # if current node is balanced
        heightDiff = leftHeight - rightHeight
        if abs(heightDiff) > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1


class binary_tree_test(unittest.TestCase):
    def test(self):
        bt = BinaryTree()
        self.assertEqual(True, bt.is_balanced())
        bt.add(5)
        self.assertEqual(True, bt.is_balanced())
        bt.add(3)
        self.assertEqual(True, bt.is_balanced())
        bt.add(1)
        self.assertEqual(False, bt.is_balanced())


