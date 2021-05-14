# 1520. Maximum Number of Non-Overlapping Substrings
# https://leetcode.com/problems/maximum-number-of-non-overlapping-substrings/

class Solution:
    def checkSubStr(self, s, i, lefts, rights):
        right = rights[ord(s[i]) - ord('a')]
        
        k = i
        while k <= right:
            if lefts[ord(s[k]) - ord('a')] < i:
                return None
            right = max(right, rights[ord(s[k]) - ord('a')])
            k += 1
        
        return right
    
    def prepareLeftRights(self, s):
        lefts = [float('inf')] * 26
        rights = [float('-inf')] * 26
        
        for i, char in enumerate(s):
            idx = ord(char) - ord('a')
            lefts[idx] = min(lefts[idx], i)
            rights[idx] = max(rights[idx], i)
        
        return lefts, rights
        
    def maxNumOfSubstrings(self, s: str) -> List[str]:
        lefts, rights = self.prepareLeftRights(s)
        res = []
        
        right = float('inf')
        prevSubStr = ''

        for i in range(len(s)):
            if i == lefts[ord(s[i]) - ord('a')]:
                newRight = self.checkSubStr(s, i, lefts, rights)
                if newRight is not None:
                    if i > right:
                        res.append(prevSubStr)
                    right = newRight
                    prevSubStr = s[i: right + 1]
        
        if prevSubStr:
            res.append(prevSubStr)
        
        return res
