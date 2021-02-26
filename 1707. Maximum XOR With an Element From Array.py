# 1707. Maximum XOR With an Element From Array
# https://leetcode.com/problems/maximum-xor-with-an-element-from-array/

class Trie:
    def __init__(self):
        self.root = {}
    
    def insertMany(self, nums):
        for num in nums:
            self.insert(num)
        
    def insert(self, num):
        node = self.root
        for bit in [(num >> i) & 1 for i in range(32)][::-1]:
            if bit not in node:
                node[bit] = {}
            node = node[bit]
    
    def query(self, num):
        node = self.root
        maximum = 0
        for bit in [(num >> i) & 1 for i in range(32)][::-1]:
            toggleBit = 1 - bit
            if toggleBit in node:
                maximum = maximum << 1 | 1
                node = node[toggleBit]
            elif bit in node:
                maximum = maximum << 1
                node = node[bit]
            else:
                return -1
        
        return maximum

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        trie = Trie()
        result = [-1] * len(queries)
        
        sortedqueries = sorted(enumerate(queries), key=lambda query: query[1][1])
        nums.sort()
        
        j = 0
        for i, (target, limit) in sortedqueries:
            while j < len(nums) and nums[j] <= limit:
                trie.insert(nums[j])
                j += 1
            
            result[i] = trie.query(target)
        
        return result
        