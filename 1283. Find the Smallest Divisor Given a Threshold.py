# 1283. Find the Smallest Divisor Given a Threshold
# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def isValid(divisor):
            total = 0
            for num in nums:
                total += ((num - 1) // divisor + 1)
            return total <= threshold

        l, r = 1, max(nums)
        while l <= r:
            div = (l + r) // 2
            if isValid(div):
                r = div - 1
            else:
                l = div + 1
        
        return l
