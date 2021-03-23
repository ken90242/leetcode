# 1052. Grumpy Bookstore Owner
# https://leetcode.com/problems/grumpy-bookstore-owner/

class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        N = len(customers)

        # first window
        prev = 0
        for i in range(X):
            prev += customers[i] if grumpy[i] else 0

        # all potential loss
        potentialLoss = 0
        for i in range(N):
            potentialLoss += customers[i] if grumpy[i] else 0

        # maximum sum in window
        maximumSave = prev
        for i in range(1, N - X + 1):
            if grumpy[i - 1]:
                prev -= customers[i - 1]
            if grumpy[i + X - 1]:
                prev += customers[i + X - 1]
            current = prev
            prev = current
            maximumSave = max(maximumSave, current)

        return sum(customers) - potentialLoss + maximumSave
