__author__ = 'Minsuk Heo'
"""
Palindrome
a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.
1-3-5-3-1 is palindrome
5-9-2 is not palindrome
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
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)

def solution(list):
    input = list.printlist()
    list.reverse()
    output = list.printlist()
    if input == output:
        return True
    else:
        return False

class LinkedListTest(unittest.TestCase):
    def test(self):
        list1 = LinkedList(1)
        list1.add(3)
        list1.add(5)
        list1.add(3)
        list1.add(1)

        list2 = LinkedList(5)
        list2.add(9)
        list2.add(2)

        self.assertEqual(True, solution(list1))
        self.assertEqual(False, solution(list2))