class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)

        # pal[i][j] = True if s[i:j+1] is a palindrome
        pal = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    if j - i <= 1 or pal[i + 1][j - 1]:
                        pal[i][j] = True

        # dp[i] = max number of non-overlapping
        # valid palindromes using s[0:i]
        dp = [0] * (n + 1)

        for end in range(1, n + 1):

            # Don't select a palindrome ending here
            dp[end] = dp[end - 1]

            # Try every possible starting position
            for start in range(end - k + 1):

                if pal[start][end - 1]:
                    dp[end] = max(
                        dp[end],
                        dp[start] + 1
                    )

        return dp[n]