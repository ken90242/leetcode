# 1231. Divide Chocolate
# https://leetcode.com/problems/divide-chocolate/

class Solution:
    def maximizeSweetness(self, sweetness: List[int], K: int) -> int:
        def canSlice(total):
            curr = 0
            slices = 0
            for sweet in sweetness:
                curr += sweet
                if curr >= total:
                    slices += 1
                    curr = 0

            return slices >= K + 1
        
        l, r = 1, sum(sweetness)
        # maximum sweetness
        while l <= r:
            mid = (l + r) // 2
            if canSlice(mid):
                l = mid + 1
            else:
                r = mid - 1
        
        return r
