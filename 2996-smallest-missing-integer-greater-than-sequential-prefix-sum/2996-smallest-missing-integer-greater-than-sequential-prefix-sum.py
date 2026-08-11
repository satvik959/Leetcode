class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        
        # Step 1: Find longest sequential prefix and its sum
        total = nums[0]
        i = 1
        while i < len(nums) and nums[i] == nums[i - 1] + 1:
            total += nums[i]
            i += 1

        # Step 2: Find smallest missing integer >= total
        num_set = set(nums)   # O(1) lookups
        while total in num_set:
            total += 1

        return total
