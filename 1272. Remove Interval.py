# 1272. Remove Interval
# https://leetcode.com/problems/remove-interval/

class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        self.intervals = intervals
    
        def remove(target):
            newIntervals = []
            deathS, deathE = target
            for interval in self.intervals:
                s, e = interval
                if e <= deathS or s >= deathE:
                    newIntervals.append(interval)
                    continue
                
                if s < deathS:
                    newIntervals.append([s, deathS])
                if e > deathE:
                    newIntervals.append([deathE, e])
                
            return newIntervals
        

        
        self.intervals = remove(toBeRemoved)
        
        return self.intervals
