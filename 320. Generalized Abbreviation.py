# 320. Generalized Abbreviation
# https://leetcode.com/problems/generalized-abbreviation/

class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.result = []
        self.dfs(word, '', True)
        self.dfs(word, '', False)
        return self.result
    
    def dfs(self, leftString, aggregate, nextShouldBeNum):
        if not leftString:
            self.result.append(aggregate)
            return

        if nextShouldBeNum:
            for i in range(1, len(leftString) + 1):
                self.dfs(leftString[i:], aggregate + str(i), False)
        else:
            for i in range(1, len(leftString) + 1):
                self.dfs(leftString[i:], aggregate + leftString[:i], True)
