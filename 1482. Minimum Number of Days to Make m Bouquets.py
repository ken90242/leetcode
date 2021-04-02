# 1482. Minimum Number of Days to Make m Bouquets
# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        def canPostpone(wait):
            count = 0
            strike = 0
            for day in bloomDay:
                if day > wait:
                    strike = 0
                else:
                    strike += 1
                    if strike == k:
                        count += 1
                        strike = 0
            return count >= m
        

        MAX_WAIT = max(bloomDay)
        l, r = 0, MAX_WAIT
        while l <= r:
            day = (l + r) // 2
            if canPostpone(day):
                r = day - 1
            else:
                l = day + 1

        ans = l if canPostpone(l) else -1
        return ans
