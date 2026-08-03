class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l = 0
        r = len(nums) - 1
        f = -1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                f = m
                r = m - 1

            elif nums[m] < target:
                l = m + 1

            else:
                r = m - 1

        l = 0
        r = len(nums) - 1
        s = -1

        while l <= r:

            m = (l + r) // 2

            if nums[m] == target:
                s = m
                l = m + 1

            elif nums[m] < target:
                l = m + 1

            else:
                r = m - 1

        return [f, s]