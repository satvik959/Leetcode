from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        cheapest = min(price for factor, price in items)

        dp = [b // cheapest for b in range(budget + 1)]

        for factor, price in items:
            gain = 0

            for f, p in items:
                if f % factor == 0:
                    gain += 1

            for b in range(budget, price - 1, -1):
                dp[b] = max(dp[b], dp[b - price] + gain)

        return dp[budget]