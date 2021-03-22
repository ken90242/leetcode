# 391. Perfect Rectangle
# https://leetcode.com/problems/perfect-rectangle/

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        points = set()
        ix = iy = float('inf')
        jx = jy = -float('inf')
        totalArea = 0
        for rectangle in rectangles:
            x1, y1 = rectangle[0], rectangle[1]
            x2, y2 = rectangle[2], rectangle[3]
            
            ix, iy = min(ix, x1), min(iy, y1)
            jx, jy = max(jx, x2), max(jy, y2)
            totalArea += (x2 - x1) * (y2 - y1)
            
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in points:
                    points.remove(corner)
                else:
                    points.add(corner)
        
        return (jx - ix) * (jy - iy) == totalArea and points == set([(ix, iy), (jx, iy), (ix, jy), (jx, jy)])
