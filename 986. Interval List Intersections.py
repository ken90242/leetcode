# 986. Interval List Intersections
# https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        result = []
        i = j = 0

        while i < len(firstList) and j < len(secondList):
            s1, e1 = firstList[i]
            s2, e2 = secondList[j]
            
            low, high = max(s1, s2), min(e1, e2)
            
            if low <= high:
                result.append([low, high])
            
            if e1 > e2:
                j += 1
            else:
                i += 1
        
        return result
