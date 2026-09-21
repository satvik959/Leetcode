from typing import List

class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        prev = [0] * k

        for num in nums:
            num %= k

            curr = [0] * k

            # Start a new subarray with only nums[i]
            curr[num] += 1

            # Extend all subarrays ending at previous index
            for r in range(k):
                new_rem = (r * num) % k
                curr[new_rem] += prev[r]

            # Add all subarrays ending here to final answer
            for r in range(k):
                result[r] += curr[r]

            prev = curr

        return result