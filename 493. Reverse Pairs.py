# 493. Reverse Pairs
# https://leetcode.com/problems/reverse-pairs/

class BinaryIndexTree:
    def __init__(self, size):
        self.table = [0] * (size + 1)
    
    def update(self, i):
        while i > 0:
            self.table[i] += 1
            i -= i & -i
    
    def query(self, i):
        ret = 0
        while i < len(self.table):
            ret += self.table[i]
            i += i & -i
        return ret

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedNums = sorted(nums)
        bit = BinaryIndexTree(len(sortedNums))

        count = 0
        for num in nums:
            count += bit.query(bisect_left(sortedNums, 2 * num + 1) + 1)
            bit.update(bisect_left(sortedNums, num) + 1)
        
        return count
