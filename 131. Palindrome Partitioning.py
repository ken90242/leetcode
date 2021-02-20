# 131. Palindrome Partitioning
# https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def partition(self, s):
        self.result = []
        self.dfs([], s)
        return self.result
    
    def isPalindrome(self, s):
        return s == s[::-1]
    
    def dfs(self, aggregate, remain):
        if not remain:
            self.result.append(aggregate)
            return
        
        # must be careful about the length's corner case... from one to the length
        for i in range(1, len(remain) + 1):
            if self.isPalindrome(remain[:i]):
                self.dfs(aggregate + [remain[:i]], remain[i:])
