# 57. Insert Interval
# https://leetcode.com/problems/insert-interval/

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        i = 0
        while i < len(intervals):
            s, e = intervals[i]
            
            if newInterval[1] < s:
                result.append(newInterval)
                newInterval = None
                break
            
            if e < newInterval[0]:
                result.append(intervals[i])
            else:
                newInterval = [min(s, newInterval[0]), max(e, newInterval[1])]
            
            i += 1
        
        if newInterval:
            result.append(newInterval)

        return result + intervals[i:]
