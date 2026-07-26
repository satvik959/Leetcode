class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        m = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        r = []

        def backtrack(i, s):
            if i == len(digits):
                r.append(s)
                return

            for c in m[digits[i]]:
                backtrack(i + 1, s + c)

        backtrack(0, "")
        return r