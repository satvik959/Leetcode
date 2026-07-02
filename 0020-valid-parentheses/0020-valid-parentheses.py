class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        d = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for c in s:
            if c == '(' or c == '{' or c == '[':
                a.append(c)
            else:
                if len(a) == 0:
                    return False

                if a[-1] != d[c]:
                    return False

                a.pop()

        return len(a) == 0