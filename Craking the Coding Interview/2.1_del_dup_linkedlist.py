__author__ = 'Minsuk Heo'
"""
Linked List
Delete Duplicate from linked list
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

    def delete_duplicate(self):
        cur = self.head
        dict = {}
        prev = None
        while cur is not None:
            if cur.val in dict:
                prev.next = cur.next
            else:
                dict[cur.val]= True
                prev = cur
            cur = cur.next

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)

class LinkedListTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        ll.add(4)
        ll.add(5)
        ll.add(6)
        ll.add(4)
        ll.add(7)
        ll.add(4)
        ll.add(6)
        ll.add(6)
        ll.delete_duplicate()
        self.assertEqual("[3, 4, 5, 6, 7]", ll.printlist())
