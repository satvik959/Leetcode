class Solution:
    def uniformArray(self, nums1: List[int]) -> bool:
        odd_count  = sum(1 for x in nums1 if x % 2 != 0)
        even_count = len(nums1) - odd_count

       
        all_odd_possible = (even_count == 0) or (odd_count >= 1)

        
        all_even_possible = (odd_count == 0) or (odd_count >= 2)

        return all_odd_possible or all_even_possible

