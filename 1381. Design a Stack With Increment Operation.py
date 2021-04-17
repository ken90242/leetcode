# 1381. Design a Stack With Increment Operation
# https://leetcode.com/problems/design-a-stack-with-increment-operation/

class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.stack = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.maxSize:
            self.stack.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if len(self.stack) > 0:
            val = self.stack.pop()
            val += self.inc[-1]
            if len(self.inc) > 1:
                self.inc[-2] += self.inc[-1]
            self.inc.pop()
            return val
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            i = min(len(self.stack), k) - 1
            self.inc[i] += val
