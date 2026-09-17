from typing import List

class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:

        n = len(arr)
        INF = float('inf')

        # best[i] = shortest target-sum subarray
        # found anywhere from index 0 to i
        best = [INF] * n

        left = 0
        total = 0
        ans = INF

        for right in range(n):

            total += arr[right]

            while total > target:
                total -= arr[left]
                left += 1

            if total == target:

                length = right - left + 1

                # Find another valid subarray completely
                # before this one
                if left > 0 and best[left - 1] != INF:
                    ans = min(
                        ans,
                        length + best[left - 1]
                    )

                # Update shortest valid subarray so far
                if right == 0:
                    best[right] = length
                else:
                    best[right] = min(best[right - 1], length)

            else:
                if right > 0:
                    best[right] = best[right - 1]

        return -1 if ans == INF else ans