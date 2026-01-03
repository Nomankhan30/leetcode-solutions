from typing import List
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}

        def dfs(i, j):
            if i >= len(grid) or j >= len(grid[0]):
                return math.inf   #make invalid path value maximum

            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(grid) - 1 and j == len(grid[0]) - 1:
                return grid[i][j]

            memo[(i, j)] = grid[i][j] + min(
                dfs(i + 1, j),
                dfs(i, j + 1)
            )

            return memo[(i, j)]

        return dfs(0, 0)
