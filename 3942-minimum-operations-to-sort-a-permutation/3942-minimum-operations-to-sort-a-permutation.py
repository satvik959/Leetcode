from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        zero = nums.index(0)
        ans = float('inf')

        # Check if array is cyclically increasing
        increasing = True

        for i in range(n):
            if nums[(zero + i) % n] != i:
                increasing = False
                break

        if increasing:
            ans = min(ans, zero)
            ans = min(ans, n - zero + 2)

        # Check if array is cyclically decreasing
        decreasing = True

        for i in range(n):
            if nums[(zero - i) % n] != i:
                decreasing = False
                break

        if decreasing:
            ans = min(ans, zero + 2)
            ans = min(ans, n - zero)

        return -1 if ans == float('inf') else ans