# 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canShip(capacity):
            days = currLoad = 0
            for weight in weights:
                if currLoad + weight <= capacity:
                    currLoad += weight
                else:
                    currLoad = weight
                    days += 1
            if currLoad > 0:
                days += 1
            return days <= D
        
        l, r = max(weights), sum(weights)

        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                r = mid - 1
            else:
                l = mid + 1
        
        return l
