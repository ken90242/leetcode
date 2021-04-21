# 308. Range Sum Query 2D - Mutable.py
# https://leetcode.com/problems/range-sum-query-2d-mutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0 for _ in range(self.n)] for _ in range(self.m)]
        self.bits = [[0 for _ in range(self.n + 1)] for _ in range(self.m + 1)]
        
        for i in range(self.m):
            for j in range(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row: int, col: int, val: int) -> None:
        diff = val - self.matrix[row][col]
        self.matrix[row][col] = val
        
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bits[i][j] += diff
                j += (j & -j)
            i += (i & -i)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sumCorner(row2, col2) + self.sumCorner(row1 - 1, col1 - 1) - self.sumCorner(row1 - 1, col2) - self.sumCorner(row2, col1 - 1)
    
    def sumCorner(self, row, col):
        total = 0

        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                total += self.bits[i][j]
                j -= (j & -j)
            i -= (i & -i)

        return total
