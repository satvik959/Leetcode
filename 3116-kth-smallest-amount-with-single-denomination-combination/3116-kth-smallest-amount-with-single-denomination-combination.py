from math import gcd
from typing import List

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Remove redundant coins: if a larger coin is divisible by a smaller one,
        # its multiples are already covered.
        coins.sort()
        filtered = []
        for c in coins:
            if all(c % x != 0 for x in filtered):
                filtered.append(c)
        coins = filtered
        
        n = len(coins)

        # Precompute lcm for every non-empty subset
        subsets = []
        for mask in range(1, 1 << n):
            l = 1
            bits = 0
            valid = True
            for i in range(n):
                if mask >> i & 1:
                    bits += 1
                    l = l * coins[i] // gcd(l, coins[i])
                    if l > 10**18:   # prevent useless overflow growth
                        valid = False
                        break
            if valid:
                subsets.append((l, bits))

        def count(x: int) -> int:
            total = 0
            for l, bits in subsets:
                if bits % 2 == 1:
                    total += x // l
                else:
                    total -= x // l
            return total

        lo, hi = 1, min(coins) * k
        while lo < hi:
            mid = (lo + hi) // 2
            if count(mid) >= k:
                hi = mid
            else:
                lo = mid + 1
        return lo
