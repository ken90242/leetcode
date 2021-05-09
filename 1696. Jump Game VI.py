# 1696. Jump Game VI
# https://leetcode.com/problems/jump-game-vi/

class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        scores = [0] * n
        scores[0] = nums[0]
        
        maxQueue = []
        heappush(maxQueue, (-nums[0], 0))
        for i in range(1, n):
            while maxQueue[0][1] < i - k:
                heappop(maxQueue)
            
            maxIdx = maxQueue[0][1]
            scores[i] = scores[maxIdx] + nums[i]
            heappush(maxQueue, (-scores[i], i))
        
        return scores[-1]
