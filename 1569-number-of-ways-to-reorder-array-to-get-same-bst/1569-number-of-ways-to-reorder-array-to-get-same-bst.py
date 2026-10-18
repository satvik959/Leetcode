from typing import List

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # combinations[i][j] = i choose j
        combinations = [[0] * (n + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            combinations[i][0] = 1
            combinations[i][i] = 1

            for j in range(1, i):
                combinations[i][j] = (
                    combinations[i - 1][j - 1]
                    + combinations[i - 1][j]
                ) % MOD

        def solve(arr):
            if len(arr) <= 2:
                return 1

            root = arr[0]

            left = []
            right = []

            for num in arr[1:]:
                if num < root:
                    left.append(num)
                else:
                    right.append(num)

            leftWays = solve(left)
            rightWays = solve(right)

            waysToMix = combinations[
                len(left) + len(right)
            ][len(left)]

            return (
                waysToMix
                * leftWays
                * rightWays
            ) % MOD

        return (solve(nums) - 1) % MOD