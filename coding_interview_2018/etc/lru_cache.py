class Node:
    def __init__(self,k,v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None


class LRU:
    def __init__(self, capacity):
        self.capacity = capacity
        self.dict = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove_node(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def add_node(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, k):
        if k in self.dict:
            return self.dict[k].val
        else:
            return -1

    def put(self, k, v):
        if k in self.dict:
            node = Node(k,v)
            self.remove_node(self.dict[k])
            self.dict[k] = node
            self.add_node(node)
        else:
            if len(self.dict) >= self.capacity:
                first = self.head.next
                second = self.head.next.next
                self.head.next = second
                second.prev = self.head
                del dict[first.key]

            node = Node(k, v)
            self.dict[k] = node
            self.add_node(node)


    def status(self):
        cur = self.head
        while cur:
            print(cur.val)
            cur = cur.next

cache = LRU(3)
cache.put(1,1)
cache.put(2,2)
cache.put(3,3)
cache.put(3,3)
#cache.put(2,2)
cache.status()
print(cache.get(1))
print(cache.get(2))
print(cache.get(3))
print(cache.get(4))