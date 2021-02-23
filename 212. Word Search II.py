# 212. Word Search II
# https://leetcode.com/problems/word-search-ii/

import collections

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.result = set()
        visited = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        self.prefixMap = collections.defaultdict(list)
        
        for word in words:
            for i in range(1, len(word) + 1):
                self.prefixMap[word[:i]].append(word)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.prefixMap[board[i][j]]:
                    visited[i][j] = True
                    self.dfs(board, visited, words, board[i][j], i, j)
                    visited[i][j] = False
        return list(self.result)
    
    def dfs(self, board, visited, words, tempString, i, j):
        # print(tempString)
        if tempString in words:
            self.result.add(tempString)

        for nextI, nextJ in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= nextI < len(board) and 0 <= nextJ < len(board[0]) and not visited[nextI][nextJ] and self.prefixMap[tempString + board[nextI][nextJ]]:
                    visited[nextI][nextJ] = True
                    self.dfs(board, visited, words, tempString + board[nextI][nextJ], nextI, nextJ)
                    visited[nextI][nextJ] = False

        
            
        
                
        
