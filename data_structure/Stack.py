import unittest

__author__ = 'Minsuk Heo'

"""
Stack
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def print_stack(self):
        print(self.items)

    def peek(self):
        return self.items[len(self.items)-1]

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class StackTest(unittest.TestCase):
    def test(self):
        st = Stack()
        self.assertTrue(st.is_empty())
        self.assertEqual(st.size(), 0)
        st.push(1)
        st.push(2)
        st.print_stack()
        st.pop()
        st.print_stack()
        st.push(3)
        self.assertEquals(st.peek(),3)
        self.assertFalse(st.is_empty())
        self.assertEqual(st.size(), 2)
