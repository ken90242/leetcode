# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            
            # latest interval has no intersection with new interval
            if newInterval[1] < s:
                result.append(newInterval)
                newInterval = None
                break
            
            # latest interval has no intersection with new interval
            if e < newInterval[0]:
                result.append(intervals[i])
            else:
                # merge the old and new interval
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
            
            i += 1
        
        # incase newInterval is the last
        if newInterval:
            result.append(newInterval)

        # incase newInterval has been inserted and remaining intervals has no intersection with it
        return result + intervals[i:]
