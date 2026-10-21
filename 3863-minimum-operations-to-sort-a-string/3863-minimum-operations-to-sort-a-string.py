class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        # Case 1: already sorted
        if all(s[i] >= s[i - 1] for i in range(1, n)):
            return 0

        # Case 2: unsorted length 2 cannot be fixed
        if n == 2:
            return -1

        smallest = min(s)
        largest = max(s)

        # Case 3: one operation is enough
        if s[0] == smallest or s[-1] == largest:
            return 1

        # Case 4: two operations
        for i in range(1, n - 1):
            if s[i] == smallest or s[i] == largest:
                return 2

        # Case 5
        return 3       