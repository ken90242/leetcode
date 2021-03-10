# 732. My Calendar III
# https://leetcode.com/problems/my-calendar-iii/

import collections

class MyCalendarThree:
    def __init__(self):
        self.timeline = collections.defaultdict(int)

    def book(self, start: int, end: int) -> int:
        self.timeline[start] += 1
        self.timeline[end] -= 1

        ongoing = maximum = 0
        for key in sorted(self.timeline):
            ongoing += self.timeline[key]
            maximum = max(maximum, ongoing)
        
        return maximum
