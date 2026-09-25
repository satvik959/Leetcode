from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:

        i = 0
        n = len(expression)

        def parse():
            nonlocal i

            result = set()
            current = {""}

            while i < n and expression[i] != '}':

                # UNION
                if expression[i] == ',':
                    result |= current
                    current = {""}
                    i += 1

                # Nested expression
                elif expression[i] == '{':
                    i += 1

                    words = parse()

                    i += 1   # skip '}'

                    current = {
                        a + b
                        for a in current
                        for b in words
                    }

                # Normal letter
                else:
                    ch = expression[i]
                    i += 1

                    current = {
                        word + ch
                        for word in current
                    }

            result |= current

            return result

        return sorted(parse())