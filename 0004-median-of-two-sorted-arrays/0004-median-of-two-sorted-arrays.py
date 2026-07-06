class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2

        if len(a) > len(b):
            a, b = b, a

        m = len(a)
        n = len(b)

        l = 0
        r = m

        while l <= r:
            i = (l + r) // 2
            j = (m + n + 1) // 2 - i

            a1 = float("-inf") if i == 0 else a[i - 1]
            a2 = float("inf") if i == m else a[i]

            b1 = float("-inf") if j == 0 else b[j - 1]
            b2 = float("inf") if j == n else b[j]

            if a1 <= b2 and b1 <= a2:
                if (m + n) % 2 == 1:
                    return max(a1, b1)
                else:
                    return (max(a1, b1) + min(a2, b2)) / 2

            elif a1 > b2:
                r = i - 1
            else:
                l = i + 1