__author__ = 'Minsuk Heo'
"""
Linked List
input: 6-3-8-1-5-9,5
output: 1-3-5-6-8-9
sort linked list with a key,
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

    def getHead(self):
        return self.head

    def printlist(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def solution(ll, key):
    cur = ll.getHead()
    pre = None
    post = None
    while cur is not None:
        if cur.val != key:
            if cur.val > key:
                if post is None:
                    post = LinkedList(cur.val)
                else:
                    post.add(cur.val)
            elif cur.val < key:
                if pre is None:
                    pre = LinkedList(cur.val)
                else:
                    pre.add(cur.val)
        cur = cur.next

    cur = pre.getHead()
    while cur.next is not None:
        cur = cur.next
    cur.next = Node(key)
    cur.next.next = post.getHead()
    return pre.printlist()




class LinkedListTest(unittest.TestCase):
    def test(self):
        ll = LinkedList(6)
        ll.add(3)
        ll.add(8)
        ll.add(1)
        ll.add(5)
        ll.add(9)
        self.assertEqual("[3, 1, 5, 6, 8, 9]", solution(ll,5))
