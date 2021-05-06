# 1306. Jump Game III
# https://leetcode.com/problems/jump-game-iii/

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:        
        VISITED = None

        def dfs(i):
            if i < 0 or i >= len(arr) or arr[i] is VISITED:
                return False

            if arr[i] == 0:
                return True

            step = arr[i]
            arr[i] = VISITED

            return dfs(i + step) or dfs(i - step)

        return dfs(start)
