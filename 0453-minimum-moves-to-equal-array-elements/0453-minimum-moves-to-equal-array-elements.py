from typing import List

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mn = min(nums)

        moves = 0

        for x in nums:
            moves += x - mn

        return moves