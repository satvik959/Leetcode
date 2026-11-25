from typing import List

class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        ranks = [nums]
        size = 1

        # Build IDs for subarrays of lengths 1, 2, 4, 8...
        while size * 2 <= n:
            prev = ranks[-1]
            ids = {}
            curr = []

            for i in range(n - 2 * size + 1):
                pair = (prev[i], prev[i + size])

                if pair not in ids:
                    ids[pair] = len(ids)

                curr.append(ids[pair])

            ranks.append(curr)
            size *= 2

        def check(length):
            p = length.bit_length() - 1
            size = 1 << p

            freq = {}

            for i in range(n - length + 1):
                key = (
                    ranks[p][i],
                    ranks[p][i + length - size]
                )

                freq[key] = freq.get(key, 0) + 1

            return 1 in freq.values()

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left