# 253. Meeting Rooms II
# https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        sortedIntervals = sorted(intervals, key=lambda ls: ls[0])
        endings = [sortedIntervals[0][1]]
        count = 1

        for i in range(1, len(sortedIntervals)):
            if endings[0] > sortedIntervals[i][0]:
                count += 1
            else:
                heappop(endings)
            
            heappush(endings, sortedIntervals[i][1])

        return count
