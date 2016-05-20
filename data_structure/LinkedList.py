__author__ = 'Minsuk Heo'
"""
Linked List
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

    def remove(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
            cur = self.head
            while cur.next is not None:
                if cur.val == item:
                    self.removeItem(item)
                    return
                cur = cur.next
            print("item does not exist in linked list")

    def removeItem(self, item):
        cur = self.head
        while cur.next is not None:
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break

    def reverse(self):
        prev = None
        cur = self.head
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev

    def printlist(self):
        cur = self.head
        while cur is not None:
            print(cur.val)
            cur = cur.next


class LinkedListTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(3)
        self.assertEqual(ll.head.val, 3)
        ll.add(4)
        self.assertEqual(ll.head.next.val, 4)
        ll.add(5)
        self.assertEqual(ll.head.next.next.val, 5)
        ll.remove(3)
        self.assertEqual(ll.head.val, 4)
        ll.remove(4)
        self.assertEqual(ll.head.val, 5)
        ll.add(6)
        self.assertEqual(ll.head.next.val, 6)
        ll.add(7)
        self.assertEqual(ll.head.next.next.val, 7)
        ll.printlist()
        ll.remove(6)
        self.assertEqual(ll.head.next.val, 7)

        ll2 = LinkedList(9)
        ll2.add(8)
        ll2.add(7)
        ll2.reverse()
        self.assertEqual(ll2.head.val, 7)
        self.assertEqual(ll2.head.next.val, 8)

