from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def digitSum(num):
            total = 0

            while num > 0:
                total += num % 10
                num //= 10

            return total

        target = sorted(nums, key=lambda x: (digitSum(x), x))

        pos = {}

        for i in range(len(nums)):
            pos[nums[i]] = i

        swaps = 0

        for i in range(len(nums)):

            if nums[i] != target[i]:

                correct_num = target[i]

                j = pos[correct_num]

                # Swap
                pos[nums[i]] = j
                pos[correct_num] = i

                nums[i], nums[j] = nums[j], nums[i]

                swaps += 1

        return swaps