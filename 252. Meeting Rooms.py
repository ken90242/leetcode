# 252. Meeting Rooms
# https://leetcode.com/problems/meeting-rooms/

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sortedIntervals = sorted(intervals, key=lambda interval: interval[0])
        for i in range(1, len(sortedIntervals)):
            if sortedIntervals[i - 1][1] > sortedIntervals[i][0]:
                return False
        
        return True
