# 1577. Number of Ways Where Square of Number Is Equal to Product of Two Numbers
# https://leetcode.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers/

class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        return self.memorizableProd(nums1, nums2) + self.memorizableProd(nums2, nums1)
    
    def memorizableProd(self, targets, candidates):
        count = 0
        memory = collections.defaultdict(int)

        for num in targets:
            if num not in memory:
                memory[num] = self.getProd(num ** 2, candidates)
            count += memory[num]
        
        return count

    def getProd(self, target, arr):
        count = 0
        prevNeed = collections.defaultdict(int)
        for num in arr:
            if num in prevNeed:
                # match how many number
                # e.g.: target is 9
                #       candidate: [1,1,8]
                #                       ^
                #                       |
                #        prevNeed: { 8: 2 }
                count += prevNeed[num]
            if target % num == 0:
                # more people need help!
                prevNeed[target // num] += 1
        return count
