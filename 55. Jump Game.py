# 55. Jump Game
# https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        start = 0
        end = nextEnd = nums[0]
        while nextEnd < len(nums) - 1:
            for i in range(start, end + 1):
                nextEnd = max(nextEnd, i + nums[i])

            if nextEnd == end:
                return False

            start, end = end + 1, nextEnd

        return True
