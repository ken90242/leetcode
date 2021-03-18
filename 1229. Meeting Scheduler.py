# 1229. Meeting Scheduler
# https://leetcode.com/problems/meeting-scheduler/

class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        def getIntersection(slot1, slot2):
            return max(slot1[0], slot2[0]), min(slot1[1], slot2[1])

        slots1.sort(key=lambda slot: slot[0])
        slots2.sort(key=lambda slot: slot[0])
        
        i = j = 0

        while i < len(slots1) and j < len(slots2):
            start, end = getIntersection(slots1[i], slots2[j])
                
            if end - start >= duration:
                return [start, start + duration]
            # if we use the end to decide which slot to slide, it doesnt matter if one of slots run out of space. cause if the case happens, there is no result
            elif slots1[i][1] < slots2[j][1]:
                i += 1
            else:
                j += 1


        return []
