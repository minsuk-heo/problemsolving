"""
         3
        /\
       2  5
      / \  \
     9  8  10
         \
         4

(9,4) : 9-2-8-4
(4,10) : 4-8-2-3-5-10
"""

class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


def print_tree(cur):
    if cur.left:
        print_tree(cur.left)
    print(cur.val)
    if cur.right:
        print_tree(cur.right)


def find_node(cur, target, path):
    if not cur:
        return []

    if cur.val == target:
        return path + [cur]
    else:
        lpath = find_node(cur.left, target, path + [cur])
        rpath = find_node(cur.right, target, path + [cur])

        if lpath is None and rpath is None:
            return []
        if lpath:
            return lpath
        if rpath:
            return rpath

def find_path(tree, n1, n2):
    # find first node
    n1_path = find_node(tree, n1, [])
    ans = []
    if not n1_path:
        return None
    else:
        n1_path = n1_path[::-1]

        for idx, cur in enumerate(n1_path):
            n2_path = find_node(cur, n2, [])
            if n2_path:
                ans = n1_path[:idx]+n2_path
                break

        return ans

head = Node(3)
head.left = Node(2)
head.right = Node(5)
head.left.left = Node(9)
head.left.right = Node(8)
head.right.right = Node(10)
head.left.right.right = Node(4)


print([node.val for node in find_path(head, 9, 4)])
print([node.val for node in find_path(head, 4, 10)])
print([node.val for node in find_path(head, 4, 4)])
print([node.val for node in find_path(head, 4, 99)])

