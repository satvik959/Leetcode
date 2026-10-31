from typing import List

class Solution:
    def uniquePaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        m = len(grid)
        n = len(grid[0])

        right = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # From the starting cell, we may initially move right or down
        right[0][1] = 1
        down[1][0] = 1

        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    continue

                # No need to move after reaching destination
                if i == m - 1 and j == n - 1:
                    continue

                if grid[i][j] == 0:
                    # Empty cell: both incoming types may choose
                    # either right or down
                    total = (right[i][j] + down[i][j]) % MOD

                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + total
                        ) % MOD

                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + total
                        ) % MOD

                else:
                    # Mirror:
                    # entered moving right -> reflected down
                    if i + 1 < m:
                        down[i + 1][j] = (
                            down[i + 1][j] + right[i][j]
                        ) % MOD

                    # entered moving down -> reflected right
                    if j + 1 < n:
                        right[i][j + 1] = (
                            right[i][j + 1] + down[i][j]
                        ) % MOD

        return (
            right[m - 1][n - 1]
            + down[m - 1][n - 1]
        ) % MOD