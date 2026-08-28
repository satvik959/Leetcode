class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 0

        # first increasing
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        if i == 0 or i == n - 1:
            return False

        # second decreasing
        dec_start = i
        while i < n - 1 and nums[i] > nums[i + 1]:
            i += 1

        if i == dec_start or i == n - 1:
            return False

        # third increasing
        inc_start = i
        while i < n - 1 and nums[i] < nums[i + 1]:
            i += 1

        return i > inc_start and i == n - 1
