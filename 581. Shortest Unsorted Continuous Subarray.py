# 581. Shortest Unsorted Continuous Subarray
# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        minimum, maximum = float('inf'), float('-inf')

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                minimum = min(minimum, nums[i])
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                maximum = max(maximum, nums[i])
        
        l = r = 0
        for l in range(len(nums)):
            if minimum < nums[l]: # 要被替換的idx
                break

        for r in range(len(nums) - 1, -1, -1):
            if maximum > nums[r]: # 要被替換的idx
                break

        return r - l + 1 if r - l > 0 else 0
