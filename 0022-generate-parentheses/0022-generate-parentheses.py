from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ans = []

        def backtrack(current, open_count, close_count):

            # If we have used all n pairs
            if len(current) == 2 * n:
                ans.append(current)
                return

            # Add opening bracket
            if open_count < n:
                backtrack(current + "(", open_count + 1, close_count)

            # Add closing bracket
            if close_count < open_count:
                backtrack(current + ")", open_count, close_count + 1)

        backtrack("", 0, 0)

        return ans