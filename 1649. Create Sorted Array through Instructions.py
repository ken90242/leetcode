# 1649. Create Sorted Array through Instructions.py
# https://leetcode.com/problems/create-sorted-array-through-instructions/submissions/

class BinaryIndexTree:
    def __init__(self, size):
        self.table = [0] * (size + 1)
    
    def update(self, i):
        i += 1
        while i < len(self.table):
            self.table[i] += 1
            i += i & -i
    
    def query(self, i):
        i += 1
        ret = 0
        while i > 0:
            ret += self.table[i]
            i -= i & -i
        
        return ret

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        m = max(instructions) + 1
        bit = BinaryIndexTree(m)

        for i in range(len(instructions)):
            leftCost = bit.query(instructions[i] - 1)
            rightCost = i - bit.query(instructions[i])
            cost += min(leftCost, rightCost)
            bit.update(instructions[i])
        
        return cost % (10 ** 9 + 7)
