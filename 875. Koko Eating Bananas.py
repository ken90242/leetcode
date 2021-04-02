# 875. Koko Eating Bananas
# https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canFinish(speed):
            total = 0
            for pile in piles:
                hour, remain = divmod(pile, speed)
                addition = 1 if remain else 0
                total = total + hour + addition
            return total <= h

        MAX_SPEED = max(piles)
        low, high = 1, MAX_SPEED

        while low <= high:
            avg = (low + high) // 2
            if canFinish(avg):
                high = avg - 1
            else:
                low = avg + 1

        return low
