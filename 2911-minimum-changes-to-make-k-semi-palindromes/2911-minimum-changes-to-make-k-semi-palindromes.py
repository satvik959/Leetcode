class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        # cost[l][r] = minimum changes needed
        # to make s[l:r+1] a semi-palindrome
        cost = [[0] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                best = float("inf")

                # d must divide length and d < length
                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Each remainder group must be a palindrome
                    for start in range(d):
                        left = l + start
                        right = l + start + (length // d - 1) * d

                        while left < right:
                            if s[left] != s[right]:
                                changes += 1

                            left += d
                            right -= d

                    best = min(best, changes)

                cost[l][r] = best

        INF = float("inf")

        # dp[parts][i] =
        # minimum cost to split first i characters
        # into exactly 'parts' substrings
        dp = [[INF] * (n + 1) for _ in range(k + 1)]

        dp[0][0] = 0

        for parts in range(1, k + 1):
            for i in range(2 * parts, n + 1):

                # last substring = s[j:i]
                # each substring must have length >= 2
                for j in range(2 * (parts - 1), i - 1):
                    if dp[parts - 1][j] != INF:
                        dp[parts][i] = min(
                            dp[parts][i],
                            dp[parts - 1][j] + cost[j][i - 1]
                        )

        return dp[k][n]