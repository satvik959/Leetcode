class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        m1 = {}
        m2 = {}

        for i in range(len(s)):
            if s[i] in m1:
                if m1[s[i]] != t[i]:
                    return False
            else:
                m1[s[i]] = t[i]

            if t[i] in m2:
                if m2[t[i]] != s[i]:
                    return False
            else:
                m2[t[i]] = s[i]

        return True