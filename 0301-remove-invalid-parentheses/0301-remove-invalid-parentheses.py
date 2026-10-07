from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:

        def isValid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1

                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = deque([s])
        visited = {s}
        result = []

        while queue:

            size = len(queue)

            for _ in range(size):

                current = queue.popleft()

                if isValid(current):
                    result.append(current)

                # Once one valid string is found at this level,
                # don't generate strings with more removals
                if result:
                    continue

                for i in range(len(current)):

                    # We only remove parentheses, not letters
                    if current[i] not in '()':
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        queue.append(new_string)

            if result:
                return result

        return [""]