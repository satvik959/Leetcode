class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"

        for i in range(n - 1):
            a = ""
            c = 1

            for j in range(1, len(s)):
                if s[j] == s[j - 1]:
                    c += 1
                else:
                    a += str(c) + s[j - 1]
                    c = 1

            a += str(c) + s[-1]
            s = a

        return s