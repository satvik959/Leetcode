from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        n = len(nums)

        # -----------------------------
        # 1. Coordinate compression
        # -----------------------------
        vals = sorted(set(nums))
        rank = {v: i for i, v in enumerate(vals)}
        m = len(vals)

        countBIT = [0] * (m + 1)
        sumBIT = [0] * (m + 1)

        def update(bit, i, delta):
            i += 1
            while i <= m:
                bit[i] += delta
                i += i & -i

        def query(bit, i):
            # sum of first i compressed positions
            ans = 0
            while i > 0:
                ans += bit[i]
                i -= i & -i
            return ans

        def kth(kth_value):
            # find compressed index of kth smallest element
            idx = 0
            step = 1 << (m.bit_length() - 1)

            while step:
                nxt = idx + step

                if nxt <= m and countBIT[nxt] < kth_value:
                    idx = nxt
                    kth_value -= countBIT[nxt]

                step >>= 1

            return idx

        # -----------------------------
        # 2. Sliding window costs
        # -----------------------------
        total_sum = 0

        for i in range(x):
            r = rank[nums[i]]

            update(countBIT, r, 1)
            update(sumBIT, r, nums[i])

            total_sum += nums[i]

        def window_cost():
            # lower median
            median_index = kth((x + 1) // 2)
            median = vals[median_index]

            left_count = query(countBIT, median_index + 1)
            left_sum = query(sumBIT, median_index + 1)

            right_count = x - left_count
            right_sum = total_sum - left_sum

            left_cost = median * left_count - left_sum
            right_cost = right_sum - median * right_count

            return left_cost + right_cost

        costs = [window_cost()]

        for start in range(1, n - x + 1):
            outgoing = nums[start - 1]
            incoming = nums[start + x - 1]

            r = rank[outgoing]
            update(countBIT, r, -1)
            update(sumBIT, r, -outgoing)
            total_sum -= outgoing

            r = rank[incoming]
            update(countBIT, r, 1)
            update(sumBIT, r, incoming)
            total_sum += incoming

            costs.append(window_cost())

        # -----------------------------
        # 3. DP to choose k windows
        # -----------------------------
        INF = 10**30

        # prev[i] = minimum cost using previous number
        # of chosen windows in first i elements
        prev = [0] * (n + 1)

        for _ in range(k):
            curr = [INF] * (n + 1)

            for i in range(1, n + 1):

                # Option 1: don't end a chosen window here
                curr[i] = curr[i - 1]

                # Option 2:
                # take window [i-x ... i-1]
                if i >= x:
                    curr[i] = min(
                        curr[i],
                        prev[i - x] + costs[i - x]
                    )

            prev = curr

        return prev[n]