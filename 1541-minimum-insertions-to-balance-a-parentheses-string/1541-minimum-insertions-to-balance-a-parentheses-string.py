class Solution:
    def minInsertions(self, s: str) -> int:
        insertions = 0
        need = 0

        for ch in s:

            if ch == '(':

                # If need is odd, one ')' is missing
                # to complete the previous pair.
                if need % 2 == 1:
                    insertions += 1
                    need -= 1

                # This '(' requires two ')'
                need += 2

            else:  # ch == ')'
                need -= 1

                # No '(' existed for this ')'
                if need < 0:
                    insertions += 1   # insert '('
                    need = 1         # inserted '(' needs one more ')'

        return insertions + need