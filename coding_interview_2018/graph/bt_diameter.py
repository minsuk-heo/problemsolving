"""
         3
        /\
       2  5
      /   \
     9    10

diameter = 5

         3
        /\
       2  5
      / \  \
     9  8  10
         \
         4

diameter = 6

"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def diameter(node):
    if not node:
        return 0
    left_diameter = longest_path(node.left)
    right_diameter = longest_path(node.right)
    return left_diameter + right_diameter + 1


def longest_path(node):
    if not node:
        return 0

    left = longest_path(node.left)
    right = longest_path(node.right)

    return max(left, right) + 1


head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(9)
head.right.right = Node(10)

print(diameter(head))

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(9)
head.left.right = Node(8)
head.right.right = Node(10)
head.left.right.right = Node(4)

print(diameter(head))

print(diameter(None))
print(diameter(Node(10)))