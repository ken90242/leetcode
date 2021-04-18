# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

class Node:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = dict()
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    
    def _add(self, node):
        prev = self.tail.prev
        next = self.tail
        prev.next = node
        node.prev = prev
        node.next = next
        next.prev = node
        
    
    def _remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
       

    def get(self, key: int) -> int:
        if key in self.dict:
            self._remove(self.dict[key])
            self._add(self.dict[key])
            return self.dict[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)
        if key in self.dict:
            self._remove(self.dict[key])
        self.dict[key] = node
        self._add(node)

        if len(self.dict) > self.capacity:
            self.dict.pop(self.head.next.key)
            self._remove(self.head.next)
