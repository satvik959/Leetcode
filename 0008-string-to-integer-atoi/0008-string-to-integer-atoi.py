class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        n = len(s)
        sign = 1
        a = 0

        while i < n and s[i] == " ":
            i += 1

        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        while i < n and s[i] == "0":
            i += 1

        while i < n and s[i].isdigit():
            a = a * 10 + int(s[i])
            i += 1

        a = a * sign

        if a < -2**31:
            return -2**31

        if a > 2**31 - 1:
            return 2**31 - 1

        return a