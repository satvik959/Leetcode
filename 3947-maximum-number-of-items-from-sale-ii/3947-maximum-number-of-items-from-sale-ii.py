from typing import List

class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)

        cheapest = min(price for factor, price in items)

        freq = [0] * (n + 1)

        for factor, price in items:
            freq[factor] += 1

        # Count eligible free items for each factor
        free = [0] * (n + 1)

        for i in range(1, n + 1):
            for j in range(i, n + 1, i):
                free[i] += freq[j]

        # Sort by price
        items.sort(key=lambda a: a[1])

        ans = 0

        for factor, price in items:
            if price >= 2 * cheapest:
                break

            limit = free[factor] - 1

            buy = min(limit, budget // price)

            ans += 2 * buy
            budget -= buy * price

        # Spend remaining budget on ordinary copies
        ans += budget // cheapest

        return ans