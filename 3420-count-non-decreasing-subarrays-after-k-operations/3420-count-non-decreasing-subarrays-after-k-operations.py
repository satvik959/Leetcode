from typing import List
from collections import deque

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)

        q = deque()

        cost = 0
        right = n - 1
        ans = 0

        for left in range(n - 1, -1, -1):

            while q and nums[q[-1]] < nums[left]:
                i = q.pop()

                if q:
                    j = q[-1]
                else:
                    j = right + 1

                cost += (j - i) * (nums[left] - nums[i])

            q.append(left)

            while cost > k:
                cost -= nums[q[0]] - nums[right]

                if q[0] == right:
                    q.popleft()

                right -= 1

            ans += right - left + 1

        return ans