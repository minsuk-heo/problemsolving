import unittest

__author__ = 'Minsuk Heo'

"""
Binary Tree

remove :
1) Node to be removed has no children.
This case is quite simple. Algorithm sets corresponding link of the parent to NULL and disposes the node.
2) Node to be removed has one child.
It this case, node is cut from the tree and algorithm links single child (with it's subtree) directly to the parent of the removed node.
3) Node to be removed has two children.
   (1) find a minimum value in the right subtree;
   (2) replace value of the node to be removed with found minimum. Now, right subtree contains a duplicate!
   (3) apply remove to the right subtree to remove a duplicate.
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

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

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

    def remove(self, item):
        if self.head.val is None:
            print ("there is no item: in BST", item)
        if self.head.val == item:
            # 1) Node to be removed has no children.
            if self.head.left is None and self.head.right is None:
                self.head = None
            # 2) Node to be removed has one child.
            elif self.head.left is None and self.head.right is not None:
                self.head = self.head.right
            # 3) Node to be removed has one child.
            elif self.head.left is not None and self.head.right is None:
                self.head = self.head.left
            # 4) Node to be removed has two children.
            else:
                self.head.val = self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else:
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print ("There is no item: ", item)
        if cur.val == item:
            # 1) Node to be removed has no children.
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            # 2) Node to be removed has one child.
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            # 3) Node to be removed has one child.
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            # 4) Node to be removed has two children.
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)


    def __most_left_val_from_right_node(self, cur):
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def __removeitem(self, parent, cur, item):
        if cur.val == item:
            if parent.left == cur:
                parent.left = None
            else:
                parent.right = None
        else:
            if cur.val > item:
                self.__removeitem(cur, cur.left, item)
            else:
                self.__removeitem(cur, cur.right, item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print (cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)
        print (cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self, cur):
        if cur.left is not None:
            self.__postorder(cur.left)

        if cur.right is not None:
            self.__postorder(cur.right)

        self.postorder_list.append(cur.val)
        print (cur.val)


class binary_tree_test(unittest.TestCase):
    def test(self):
        bt = BinaryTree()
        bt.add(5)
        bt.add(3)
        bt.add(4)
        bt.add(1)
        bt.add(7)
        print("pre order")
        bt.preorder_traverse()
        self.assertEqual(bt.preorder_list, [5,3,1,4,7])

        print("in order")
        bt.inorder_traverse()
        self.assertEqual(bt.inorder_list, [1,3,4,5,7])

        print("post order")
        bt.postorder_traverse()
        self.assertEqual(bt.postorder_list, [1,4,3,7,5])

        print ("bt root remove")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(50)
        bt_root_remove_test.add(70)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [70,50])

        print ("bt root remove2")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(50)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [50])

        print ("bt root remove3")
        bt_root_remove_test = BinaryTree()
        bt_root_remove_test.add(60)
        bt_root_remove_test.add(70)
        bt_root_remove_test.remove(60)
        bt_root_remove_test.preorder_traverse()
        self.assertEqual(bt_root_remove_test.preorder_list, [70])

        print ("bt left remove 1")
        bt_left_remove_test_1 = BinaryTree()
        bt_left_remove_test_1.add(60)
        bt_left_remove_test_1.add(50)
        bt_left_remove_test_1.add(70)
        bt_left_remove_test_1.remove(50)
        bt_left_remove_test_1.preorder_traverse()
        self.assertEqual(bt_left_remove_test_1.preorder_list, [60,70])

        print ("bt left remove 2")
        bt_left_remove_test_2_left = BinaryTree()
        bt_left_remove_test_2_left.add(60)
        bt_left_remove_test_2_left.add(50)
        bt_left_remove_test_2_left.add(70)
        bt_left_remove_test_2_left.add(40)
        bt_left_remove_test_2_left.remove(50)
        bt_left_remove_test_2_left.preorder_traverse()
        self.assertEqual(bt_left_remove_test_2_left.preorder_list, [60,40,70])

        print ("bt right remove 2")
        bt_left_remove_test_2_right = BinaryTree()
        bt_left_remove_test_2_right.add(60)
        bt_left_remove_test_2_right.add(50)
        bt_left_remove_test_2_right.add(70)
        bt_left_remove_test_2_right.add(55)
        bt_left_remove_test_2_right.remove(50)
        bt_left_remove_test_2_right.preorder_traverse()
        self.assertEqual(bt_left_remove_test_2_right.preorder_list, [60,55,70])

        print ("bt right remove 1")
        bt_right_remove_test_1 = BinaryTree()
        bt_right_remove_test_1.add(60)
        bt_right_remove_test_1.add(50)
        bt_right_remove_test_1.add(70)
        bt_right_remove_test_1.remove(70)
        bt_right_remove_test_1.preorder_traverse()
        self.assertEqual(bt_right_remove_test_1.preorder_list, [60,50])

        print ("bt right remove 2")
        bt_right_remove_test_2_left = BinaryTree()
        bt_right_remove_test_2_left.add(60)
        bt_right_remove_test_2_left.add(50)
        bt_right_remove_test_2_left.add(70)
        bt_right_remove_test_2_left.add(65)
        bt_right_remove_test_2_left.remove(70)
        bt_right_remove_test_2_left.preorder_traverse()
        self.assertEqual(bt_right_remove_test_2_left.preorder_list, [60,50,65])

        print ("bt right remove 2")
        bt_right_remove_test_2_right = BinaryTree()
        bt_right_remove_test_2_right.add(60)
        bt_right_remove_test_2_right.add(50)
        bt_right_remove_test_2_right.add(70)
        bt_right_remove_test_2_right.add(75)
        bt_right_remove_test_2_right.remove(70)
        bt_right_remove_test_2_right.preorder_traverse()
        self.assertEqual(bt_right_remove_test_2_right.preorder_list, [60,50,75])

        print ("bt left remove 3")
        bt_left_remove_test_3 = BinaryTree()
        bt_left_remove_test_3.add(60)
        bt_left_remove_test_3.add(50)
        bt_left_remove_test_3.add(70)
        bt_left_remove_test_3.add(40)
        bt_left_remove_test_3.add(55)
        bt_left_remove_test_3.add(52)
        bt_left_remove_test_3.remove(50)
        bt_left_remove_test_3.preorder_traverse()
        self.assertEqual(bt_left_remove_test_3.preorder_list, [60,52,40,55,70])

        print("BST search test")
        bt_search_test = BinaryTree()
        bt_search_test.add(60)
        bt_search_test.add(50)
        bt_search_test.add(70)
        bt_search_test.add(40)
        bt_search_test.add(55)
        bt_search_test.add(52)
        self.assertTrue(bt_search_test.search(60))
        self.assertTrue(bt_search_test.search(50))
        self.assertTrue(bt_search_test.search(70))
        self.assertTrue(bt_search_test.search(40))
        self.assertTrue(bt_search_test.search(55))
        self.assertTrue(bt_search_test.search(52))
        self.assertFalse(bt_search_test.search(61))
        self.assertFalse(bt_search_test.search(81))


