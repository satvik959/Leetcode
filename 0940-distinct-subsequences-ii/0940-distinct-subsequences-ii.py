class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # dp[i] = distinct subsequences (including empty) using s[0..i-1]
        dp = [0] * (n + 1)
        dp[0] = 1  # empty subsequence

        # Tracks the dp value at the last occurrence of each character
        last = {}  # char -> dp value when char was last seen

        for i in range(1, n + 1):
            c = s[i - 1]
            dp[i] = (2 * dp[i - 1]) % MOD

            # Subtract duplicates introduced by previous occurrence of c
            if c in last:
                dp[i] = (dp[i] - last[c]) % MOD

            # Record dp[i-1] as the "baseline" for this character
            last[c] = dp[i - 1]

        # Subtract 1 to exclude the empty subsequence
        return (dp[n] - 1) % MOD
