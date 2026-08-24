from typing import List

class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        n = len(stones)
        
        # Prefix sums
        for i in range(1, n):
            stones[i] += stones[i - 1]
        
        # dp represents the best score difference starting from position i
        dp = stones[-1]
        
        # Work backwards
        for i in range(n - 2, 0, -1):
            dp = max(dp, stones[i] - dp)
        
        return dp
