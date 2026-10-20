from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)

        # Maximum value before each position
        pref_max = [0] * (n + 1)

        for i in range(n):
            pref_max[i + 1] = max(pref_max[i], nums[i])

        # Minimum value from each position to the end
        suff_min = [10**9] * (n + 1)

        for i in range(n - 1, -1, -1):
            suff_min[i] = min(nums[i], suff_min[i + 1])

        # Number of strict drops:
        # nums[i-1] > nums[i]
        drops = [0] * n

        for i in range(1, n):
            drops[i] = drops[i - 1]

            if nums[i - 1] > nums[i]:
                drops[i] += 1

        def valid(k):
            for start in range(0, n, k):

                end = start + k - 1

                # Drops inside this block
                count = drops[end] - drops[start]

                # Check circular edge:
                # last element -> first element
                if nums[end] > nums[start]:
                    count += 1

                # More than one circular drop means
                # no rotation can sort this block
                if count > 1:
                    return False

                # Everything before this block must be
                # <= everything from this block onward
                if pref_max[start] > suff_min[start]:
                    return False

            return True

        ans = 0

        # Check only divisors of n
        i = 1

        while i * i <= n:
            if n % i == 0:

                if valid(i):
                    ans += i

                other = n // i

                if other != i and valid(other):
                    ans += other

            i += 1

        return ans