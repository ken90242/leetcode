# 1234. Replace the Substring for Balanced String
# https://leetcode.com/problems/replace-the-substring-for-balanced-string/

class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        res = N = len(s)
        l = r = 0
        
        # j用來找到在下一個能平衡的最近距離的window，但size可能很大
        while r < len(s):
            count[s[r]] -= 1
            # i用來挑戰再平衡下的最小window
            while l < len(s) and all(count[char] <= N // 4 for char in 'QWER'):
                res = min(res, r - l + 1)
                count[s[l]] += 1
                l += 1
            r += 1
        
        return res
