__author__ = 'Minsuk Heo'
"""
Linked List
k th node value from last node
"""
import unittest

class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)

    def kth_element_from_last(self,k):
        p1 = self.head
        p2 = self.head
        if k != 0:
            for i in range(k):
                p2 = p2.next
            # over flow k is greater than linkedlist length
            if p2 is None:
                return None
        # run until p2 reach the end
        while p2.next is not None:
            p2 = p2.next
            p1 = p1.next
        # since p2 - p1 is the k, now p1 position is the k th from last node
        return p1.val


class LinkedListTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)
        self.assertEqual(4, ll.kth_element_from_last(0))
        self.assertEqual(7, ll.kth_element_from_last(1))
        self.assertEqual(4, ll.kth_element_from_last(2))
        self.assertEqual(6, ll.kth_element_from_last(3))
        self.assertEqual(5, ll.kth_element_from_last(4))
        self.assertEqual(4, ll.kth_element_from_last(5))
        self.assertEqual(3, ll.kth_element_from_last(6))
        self.assertEqual(None, ll.kth_element_from_last(7))
