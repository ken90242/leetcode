# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n):
        self.result = []

        self.dfs(n, n, '')

        return self.result
    
    def dfs(self, left, right, tmp):
        if left == right == 0:
            self.result.append(tmp)
            return
        
        if left > right:
            return

        if left > 0:
            self.dfs(left - 1, right, tmp + '(')
        if right > 0: 
            self.dfs(left, right - 1, tmp + ')')
