# 460. LFU Cache
# https://leetcode.com/problems/lfu-cache/

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.used = 1
        self.next = None
        self.prev = None

class DLink:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def add(self, node):
        self.size += 1
        next = self.head.next
        prev = self.head
        node.next = next
        node.prev = prev
        prev.next = node
        next.prev = node
    
    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
        self.size -= 1
    
    def removeLast(self):
        if self.size > 0:
            node = self.tail.prev
            self.remove(node)
            return node
        return None

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.freq2DLinks = collections.defaultdict(DLink)
        self.key2Node = {}
        self.minFreq = 1
        self.size = 0
    
    def update(self, node):
        # will update by get or put existing values
        self.freq2DLinks[node.used].remove(node)
        if node.used == self.minFreq and self.freq2DLinks[node.used].size == 0:
            self.minFreq += 1
        node.used += 1
        self.freq2DLinks[node.used].add(node)

    def get(self, key: int) -> int:
        if key in self.key2Node:
            node = self.key2Node[key]
            self.update(node)
            return node.value

        return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key2Node:
            node = self.key2Node[key]
            node.value = value
            self.update(node)
        else:
            node = Node(key, value)
            self.key2Node[key] = node

            if self.size == self.capacity:
                minList = self.freq2DLinks[self.minFreq]
                self.key2Node.pop(minList.removeLast().key)
                self.size -= 1

            self.size += 1
            # everytime a new incoming elemnet: minFreq = 1
            self.minFreq = 1
            self.freq2DLinks[node.used].add(node)
