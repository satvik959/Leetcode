from typing import List

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        # Segment tree stores:
        # tree_sum[node] = sum of distinct counts
        # tree_sq[node]  = sum of squares of distinct counts
        tree_sum = [0] * (4 * n)
        tree_sq = [0] * (4 * n)
        lazy = [0] * (4 * n)

        def apply(node, l, r, val):
            length = r - l + 1

            # (x + val)^2 = x^2 + 2*x*val + val^2
            tree_sq[node] = (
                tree_sq[node]
                + 2 * val * tree_sum[node]
                + val * val * length
            ) % MOD

            tree_sum[node] = (
                tree_sum[node] + val * length
            ) % MOD

            lazy[node] += val

        def push(node, l, r):
            if lazy[node] == 0 or l == r:
                return

            mid = (l + r) // 2

            apply(node * 2, l, mid, lazy[node])
            apply(node * 2 + 1, mid + 1, r, lazy[node])

            lazy[node] = 0

        def update(node, l, r, ql, qr):
            if qr < l or r < ql:
                return

            if ql <= l and r <= qr:
                apply(node, l, r, 1)
                return

            push(node, l, r)

            mid = (l + r) // 2

            update(node * 2, l, mid, ql, qr)
            update(node * 2 + 1, mid + 1, r, ql, qr)

            tree_sum[node] = (
                tree_sum[node * 2] +
                tree_sum[node * 2 + 1]
            ) % MOD

            tree_sq[node] = (
                tree_sq[node * 2] +
                tree_sq[node * 2 + 1]
            ) % MOD

        last = {}
        ans = 0

        for i, num in enumerate(nums):

            prev = last.get(num, -1)

            # nums[i] becomes a new distinct element
            # for starts prev+1 ... i
            update(1, 0, n - 1, prev + 1, i)

            last[num] = i

            # Sum of squares for all subarrays ending at i
            ans = (ans + tree_sq[1]) % MOD

        return ans