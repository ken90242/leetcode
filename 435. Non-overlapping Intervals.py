# 435. Non-overlapping Intervals
# https://leetcode.com/problems/non-overlapping-intervals/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        # always pick the interval with the earliest end time.
        # becausethe interval with the earliest end time produces the maximal capacity to hold rest intervals

        '''
        E.g.
        	Suppose current earliest end time of the rest intervals is x. 
        	Then available time slot left for other intervals is [x:].
        	If we choose another interval with end time y,
        	then available time slot would be [y:].
        	Since x ≤ y, there is no way [y:] can hold more intervals then [x:]. Thus, the heuristic holds.
        '''
        ending = None
        count = 0
        for s, e in intervals:
            if ending is None or ending <= s:
                ending = e
            else:
                count += 1
        
        return count
