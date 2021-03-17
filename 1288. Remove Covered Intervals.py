# 1288. Remove Covered Intervals
# https://leetcode.com/problems/remove-covered-intervals/


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals in such an order that only previous ones are possible to cover current one.
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        
        count = 0
        prev = None
        for interval in intervals:
            if not prev or prev[0] > interval[0] or interval[1] > prev[1]:
                count += 1
                prev = interval
        
        return count
