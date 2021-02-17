# 526. Beautiful Arrangement
# https://leetcode.com/problems/beautiful-arrangement/

class Solution:
    def countArrangement(self, n: int) -> int:
        count = 0
        stack = [(1, list(range(n + 1)))]
        
        while stack:
            start, perm = stack.pop()

            if start == n + 1:
                count += 1
                continue

            for i in range(start, n + 1):
            	# not affect other array in the stack
                newPerm = perm.copy()
                newPerm[i], newPerm[start] = newPerm[start], newPerm[i]
                if newPerm[start] % start == 0 or start % newPerm[start] == 0:
                    stack.append((start + 1, newPerm))
            
        
        return count
