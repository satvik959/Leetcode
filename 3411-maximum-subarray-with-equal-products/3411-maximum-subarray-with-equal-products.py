from typing import List
from math import gcd, lcm

class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0

        for i in range(len(nums)):
            product = 1
            g = 0
            L = 1

            for j in range(i, len(nums)):
                product *= nums[j]
                g = gcd(g, nums[j])
                L = lcm(L, nums[j])

                if product == g * L:
                    ans = max(ans, j - i + 1)

        return ans