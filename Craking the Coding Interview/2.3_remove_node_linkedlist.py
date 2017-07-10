__author__ = 'Minsuk Heo & Chris Jones'
"""
Linked List
"""
class Node:
    def __init__(self, item):
        self.val = item
        self.next = None

# Class to handle the linked list options
class LinkedList:
    def __init__(self, item):
        self.head = Node(item)

    # Adds a value to the linked list
    def add(self, item):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(item)

    # removes a value from teh linked list
    def remove_item(self, item):
        if self.head.val == item:
            self.head = self.head.next
        else:
         cur = self.head
         while cur.next is not None:
            if cur.next.val == item:
                next_node = cur.next.next
                cur.next = next_node
                break
            cur = cur.next

    def print_list(self):
        cur = self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur = cur.next
        return str(res)


ll = LinkedList(9)
ll.add(5)
ll.add(8)
ll.add(7)
ll.add(6)
ll.remove_item(6)
print(ll.print_list())
