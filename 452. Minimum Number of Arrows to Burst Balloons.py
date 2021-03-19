# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        '''
            one could always track the end of the current balloon,
            and ignore all the balloons which end before it.

            Once the current balloon is ended (meaning: the next balloon starts after the current balloon),
            one has to increase the number of arrows by one and start to track the end of the next balloon.
        '''
        if not points:
            return 0


        points.sort(key=lambda point: point[1])        

        count = 1
        prevE = points[0][1]
        for s, e in points[1:]:            
            if s > prevE:
                count += 1
                prevE = e
        
        return count
