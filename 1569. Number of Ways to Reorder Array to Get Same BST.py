# 1569. Number of Ways to Reorder Array to Get Same BST
# https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(nums):
            if len(nums) <= 1:
                return 1
            root = nums[0]
            left = [num for num in nums if num < root]
            right = [num for num in nums if num > root]
            ans = comb(len(left) + len(right), len(right)) * f(left) * f(right)
            return ans

        return (f(nums) - 1) % (10 ** 9 + 7)
