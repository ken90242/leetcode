# 666. Path Sum IV
# https://leetcode.com/problems/path-sum-iv/

class Solution:
    def pathSum(self, nums: List[int]) -> int:
        q = {}
        for num in nums:
            d, num = divmod(num, 100)
            p, v = divmod(num, 10)
            q[(d, p)] = v

        ans = 0
        def dfs(d, p, total):
            nonlocal ans

            left = p * 2 - 1
            right = p * 2
            total += q[(d, p)]
            
            if not (d + 1, left) in q and not (d + 1, right) in q:
                ans += total
                return
            
            if (d + 1, left) in q:
                dfs(d + 1, left, total)
            
            if (d + 1, right) in q:
                dfs(d + 1, right, total)

        dfs(1, 1, 0)
        
        return ans
