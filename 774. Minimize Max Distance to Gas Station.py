# 774. Minimize Max Distance to Gas Station
# https://leetcode.com/problems/minimize-max-distance-to-gas-station/

class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def getMaxDist():
            ans = 0
            for i in range(1, len(stations)):
                ans = max(ans, stations[i] - stations[i - 1])
            return ans
                
        def canDo(penalty):
            need = 0
            for i in range(1, len(stations)):
                distance = stations[i] - stations[i - 1]
                need += math.ceil(distance / penalty) - 1
            
            return need <= k

        l, r = 0, getMaxDist()
        while r - l > 10 ** -6:
            penalty = (l + r) / 2
            if canDo(penalty):
                r = penalty - 10 ** -6
            else:
                l = penalty + 10 ** -6

        return r
