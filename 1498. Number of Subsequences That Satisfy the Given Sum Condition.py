# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        mod = 10 ** 9 + 7
        count = 0
        
        while i < len(nums):
            while i <= j and nums[i] + nums[j] > target:
                j -= 1

            if i <= j:
                count += pow(2, j - i, mod)
                count %= mod
            i += 1
    
        return count
