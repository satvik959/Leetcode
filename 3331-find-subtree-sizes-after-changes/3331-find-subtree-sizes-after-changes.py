from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]

        # nearest ancestor currently on DFS path for each character
        last = [-1] * 26

        # preorder of original tree
        order = []

        # (node, entering, previous_value)
        stack = [(0, True, -1)]

        while stack:
            node, entering, previous = stack.pop()
            c = ord(s[node]) - ord('a')

            if entering:
                order.append(node)

                # closest ancestor with same character
                if node != 0 and last[c] != -1:
                    new_parent[node] = last[c]

                old = last[c]
                last[c] = node

                # restore this character when leaving node
                stack.append((node, False, old))

                for child in reversed(children[node]):
                    stack.append((child, True, -1))

            else:
                last[c] = previous

        # Every node initially contributes 1 to its own subtree
        ans = [1] * n

        # Children must contribute before ancestors
        for node in reversed(order[1:]):
            ans[new_parent[node]] += ans[node]

        return ans