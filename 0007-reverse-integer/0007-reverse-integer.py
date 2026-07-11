class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        s = -1 if x < 0 else 1
        x = abs(x)

        while x > 0:
            d = x % 10
            x = x // 10

            if a > (2**31 - 1 - d) // 10:
                return 0

            a = a * 10 + d

        return a * s