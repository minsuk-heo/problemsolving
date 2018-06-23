"""
         3
        / \
       2  5

balanced = True

         3
        / \
       2  5
      / \
     9  8
         \
         4

balanced = False

         3
        /\
       2  5
      / \  \
     9  8  10
         \
         4

balanced = True

"""


class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def get_depth(node):
    if not node:
        return 0

    left = get_depth(node.left)
    right = get_depth(node.right)

    if left == -1 or right == -1:
        return -1
    else:
        if abs(left - right) > 1:
            return -1
        else:
            return max(left, right)+1


def check_balanced_bt(node):
    if not node:
        return True

    if get_depth(node) == -1:
        return False
    else:
        return True

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.right = Node(6)

print(check_balanced_bt(head))

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.right.right = Node(6)
head.right.right.right = Node(6)

print(check_balanced_bt(head))