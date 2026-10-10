from typing import List

class Solution:
    def minSumSquareDiff(
        self,
        nums1: List[int],
        nums2: List[int],
        k1: int,
        k2: int
    ) -> int:

        k = k1 + k2

        diffs = []

        for i in range(len(nums1)):
            diffs.append(abs(nums1[i] - nums2[i]))

        # If we can make every difference zero
        if sum(diffs) <= k:
            return 0

        max_diff = max(diffs)

        freq = [0] * (max_diff + 1)

        for d in diffs:
            freq[d] += 1

        # Reduce largest differences first
        for d in range(max_diff, 0, -1):

            if k == 0:
                break

            if freq[d] == 0:
                continue

            if k >= freq[d]:
                k -= freq[d]

                freq[d - 1] += freq[d]
                freq[d] = 0

            else:
                freq[d] -= k
                freq[d - 1] += k
                k = 0

        ans = 0

        for d in range(len(freq)):
            ans += freq[d] * d * d

        return ans