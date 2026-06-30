class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        a = set()
        l = 0
        m = 0

        for r in range(len(s)):
            while s[r] in a:
                a.remove(s[l])
                l += 1

            a.add(s[r])
            m = max(m, r - l + 1)

        return m