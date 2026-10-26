from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] > 0:

                    stack = [(r, c)]
                    island_sum = 0

                    while stack:
                        x, y = stack.pop()

                        if (
                            x < 0 or x >= rows or
                            y < 0 or y >= cols or
                            grid[x][y] == 0
                        ):
                            continue

                        island_sum += grid[x][y]

                        # Mark as visited
                        grid[x][y] = 0

                        stack.append((x + 1, y))
                        stack.append((x - 1, y))
                        stack.append((x, y + 1))
                        stack.append((x, y - 1))

                    if island_sum % k == 0:
                        count += 1

        return count