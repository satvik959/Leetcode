class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        a = [""] * numRows
        r = 0
        d = 1

        for c in s:
            a[r] += c

            if r == 0:
                d = 1
            elif r == numRows - 1:
                d = -1

            r += d

        return "".join(a)