"""
implement queue using two stacks
"""
import unittest

class Stack:
    def __init__(self):
        self.items = []
        self.max = 3

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class myQueue:
    def __init__(self):
        self.st1 = Stack()
        self.st2 = Stack()

    def enqueue(self, item):
        self.st1.push(item)

    def dequeue(self):
        if self.st2.is_empty():
            while self.st1.is_empty() is False:
                self.st2.push(self.st1.pop())

        return self.st2.pop()

class test(unittest.TestCase):
    def test(self):
        myq = myQueue()
        myq.enqueue(1)
        myq.enqueue(2)
        self.assertEqual(1, myq.dequeue())
        myq.enqueue(3)
        self.assertEqual(2, myq.dequeue())