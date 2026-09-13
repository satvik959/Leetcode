from typing import List
from collections import defaultdict

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:

        ones1 = []
        ones2 = []

        n = len(img1)

        for i in range(n):
            for j in range(n):
                if img1[i][j] == 1:
                    ones1.append((i, j))

                if img2[i][j] == 1:
                    ones2.append((i, j))

        count = defaultdict(int)
        ans = 0

        for r1, c1 in ones1:
            for r2, c2 in ones2:

                shift = (r2 - r1, c2 - c1)

                count[shift] += 1

                ans = max(ans, count[shift])

        return ans