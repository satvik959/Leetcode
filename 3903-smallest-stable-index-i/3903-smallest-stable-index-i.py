from typing import List

class Solution:
    def firstStableIndex(self, nums: List[int], k: int) -> int:
        n = len(nums)
        suf = nums[:]

        # Calculate suffix minimums
        for i in range(n - 2, -1, -1):
            suf[i] = min(nums[i], suf[i + 1])

        mx = nums[0]

        # Calculate prefix maximum and check stability
        for i in range(n):
            mx = max(mx, nums[i])

            if mx - suf[i] <= k:
                return i

        return -1