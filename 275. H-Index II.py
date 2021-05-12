275. H-Index II
https://leetcode.com/problems/h-index-ii/

class Solution:
    def hIndex(self, citations: List[int]) -> int:

        n = len(citations)
        start, end = 0, n - 1
        while start <= end:
            h = (start + end) // 2
            if citations[h] < n - h:
                start = h + 1
            else: # lower bar
                end = h - 1
        return n - start
