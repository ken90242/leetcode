# 336. Palindrome Pairs
# https://leetcode.com/problems/palindrome-pairs/

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word2idx = { word: i for i, word in enumerate(words) }
        ans = []
        
        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix, suffix = word[:j], word[j:]
                prefixReverse, suffixReverse = prefix[::-1], suffix[::-1]
                
                # e.g. <need>aa<sufix>, aa = prefix
                if prefix == prefixReverse:
                    need = suffixReverse
                    if need != word and need in word2idx:
                        ans.append([word2idx[need], i])
                # e.g. <prefix>aa<need>, aa = suffix
                # skip "" suffix, because "" will used as prefix for matching word
                if j != len(word) and suffix == suffixReverse:
                    need = prefixReverse
                    if need != word and need in word2idx:
                        ans.append([i, word2idx[need]])
                        
        return ans
