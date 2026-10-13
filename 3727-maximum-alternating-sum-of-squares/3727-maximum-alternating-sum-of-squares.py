from typing import List

class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        squares = []

        for num in nums:
            squares.append(num * num)

        squares.sort()

        n = len(nums)
        negative_count = n // 2

        ans = 0

        for i in range(n):
            if i < negative_count:
                ans -= squares[i]
            else:
                ans += squares[i]

        return ans