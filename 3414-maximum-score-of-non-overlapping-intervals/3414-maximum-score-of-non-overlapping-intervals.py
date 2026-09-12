from typing import List
from bisect import bisect_left


class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        # Add original index
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append((l, r, w, i))

        # Sort by right endpoint
        arr.sort(key=lambda x: x[1])

        n = len(arr)

        # Store all right endpoints
        ends = [arr[i][1] for i in range(n)]

        # prev[i] = number of intervals ending strictly before arr[i] starts
        prev = [0] * n

        for i in range(n):
            l = arr[i][0]

            # First end >= l
            # Therefore all positions before this have end < l
            prev[i] = bisect_left(ends, l)

        # dp[i][k]
        # best result using first i intervals and at most k selections
        #
        # Each state = (maximum_score, tuple_of_indices)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        def better(a, b):
            # Higher score wins
            if a[0] > b[0]:
                return a

            if b[0] > a[0]:
                return b

            # Same score -> lexicographically smaller indices win
            if a[1] < b[1]:
                return a

            return b

        for i in range(1, n + 1):

            l, r, w, original_index = arr[i - 1]

            for k in range(1, 5):

                # Option 1: don't take current interval
                skip = dp[i - 1][k]

                # Option 2: take current interval
                old_score, old_indices = dp[prev[i - 1]][k - 1]

                # Keep indices sorted for lexicographical comparison
                new_indices = tuple(
                    sorted(old_indices + (original_index,))
                )

                take = (
                    old_score + w,
                    new_indices
                )

                dp[i][k] = better(skip, take)

        return list(dp[n][4][1])