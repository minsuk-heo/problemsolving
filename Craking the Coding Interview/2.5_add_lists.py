__author__ = 'Minsuk Heo'
"""
Linked List
input: 7-1-6, 5-9-2 # 617 + 295
output: 912
add two linked list and return int value
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

def solution(list1, list2):
    v1 = list1.getHead()
    v2 = list2.getHead()
    carry = 0
    while v1 is not None:
        val = ((v1.val + v2.val) % 10) + carry
        carry = (v1.val + v2.val) // 10
        v1.val = val
        v1 = v1.next
        v2 = v2.next

    cur = list1.getHead()
    val = 0
    mul = 1
    while cur is not None:
        val = val + (cur.val * mul)
        mul = mul * 10
        cur = cur.next
    return val

class LinkedListTest(unittest.TestCase):
    def test(self):
        list1 = LinkedList(7)
        list1.add(1)
        list1.add(6)

        list2 = LinkedList(5)
        list2.add(9)
        list2.add(2)

        self.assertEqual(912, solution(list1,list2))