class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)

        first = list(set1 - set2)
        second = list(set2 - set1)

        return [first, second]
