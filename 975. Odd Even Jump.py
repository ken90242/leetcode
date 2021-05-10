975. Odd Even Jump
https://leetcode.com/problems/odd-even-jump/

class Solution:
    def oddEvenJumps(self, arr: List[int]) -> int:
        n = len(arr)
        nextHigher, nextLower = [0] * n, [0] * n
        
        stack = []
        for v, i in sorted([[v, i] for i, v in enumerate(arr)]):
            while stack and stack[-1] < i:
                nextHigher[stack.pop()] = i
            stack.append(i)
        
        
        stack = []
        for v, i in sorted([[-v, i] for i, v in enumerate(arr)]):
            while stack and stack[-1] < i:
                nextLower[stack.pop()] = i
            stack.append(i)
        
        successfulOddStartingPoints = [0] * n
        successfulEvenStartingPoints = [0] * n
        successfulOddStartingPoints[-1] = successfulEvenStartingPoints[-1] = 1
        
        for i in range(n - 1)[::-1]:
            successfulOddStartingPoints[i] = successfulEvenStartingPoints[nextHigher[i]]
            successfulEvenStartingPoints[i] = successfulOddStartingPoints[nextLower[i]]
        
        return sum(successfulOddStartingPoints)
