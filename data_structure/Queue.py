import unittest

__author__ = 'Minsuk Heo'

"""
Queue
"""


class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def print_queue(self):
        print(self.items)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)

class QueueTest(unittest.TestCase):
    def test(self):
        queue = Queue()
        self.assertTrue(queue.is_empty())
        queue.enqueue(1)
        self.assertEqual(queue.size(),1)
        queue.enqueue(2)
        self.assertEqual(queue.size(),2)
        queue.print_queue()
        queue.dequeue()
        self.assertEqual(queue.size(),1)
        queue.print_queue()
        self.assertFalse(queue.is_empty())
