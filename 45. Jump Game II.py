# 45. Jump Game II
# https://leetcode.com/problems/jump-game-ii/


class Solution:
    def jump(self, nums: List[int]) -> int:
    	end = farthest = count = 0

    	for i in range(len(nums) - 1):
    		farthest = max(farthest, i + nums[i])

    		if i == end:
    			count += 1
    			end = farthest

    	return count
