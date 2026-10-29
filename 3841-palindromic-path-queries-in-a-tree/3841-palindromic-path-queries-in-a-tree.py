from typing import List

class Solution:
    def palindromePath(
        self,
        n: int,
        edges: List[List[int]],
        s: str,
        queries: List[str]
    ) -> List[bool]:

        graph = [[] for _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def charMask(ch):
            return 1 << (ord(ch) - ord('a'))

        # -----------------------------------
        # 1. DFS information
        # -----------------------------------

        parent = [0] * n
        depth = [0] * n
        tin = [0] * n
        size = [1] * n

        # XOR mask from root to node
        rootMask = [0] * n

        parent[0] = 0
        rootMask[0] = charMask(s[0])

        order = []
        stack = [0]

        while stack:
            u = stack.pop()

            tin[u] = len(order)
            order.append(u)

            for v in graph[u]:
                if v == parent[u]:
                    continue

                parent[v] = u
                depth[v] = depth[u] + 1
                rootMask[v] = rootMask[u] ^ charMask(s[v])

                stack.append(v)

        # subtree sizes
        for u in reversed(order[1:]):
            size[parent[u]] += size[u]

        # -----------------------------------
        # 2. Binary lifting for LCA
        # -----------------------------------

        LOG = n.bit_length()

        up = [[0] * n for _ in range(LOG)]

        for u in range(n):
            up[0][u] = parent[u]

        for j in range(1, LOG):
            for u in range(n):
                up[j][u] = up[j - 1][up[j - 1][u]]

        def lca(u, v):

            if depth[u] < depth[v]:
                u, v = v, u

            diff = depth[u] - depth[v]

            for j in range(LOG):
                if diff & (1 << j):
                    u = up[j][u]

            if u == v:
                return u

            for j in range(LOG - 1, -1, -1):
                if up[j][u] != up[j][v]:
                    u = up[j][u]
                    v = up[j][v]

            return parent[u]

        # -----------------------------------
        # 3. Fenwick Tree for range XOR
        # -----------------------------------

        bit = [0] * (n + 2)

        def add(index, value):
            index += 1

            while index < len(bit):
                bit[index] ^= value
                index += index & -index

        def rangeXor(left, right, value):
            add(left, value)
            add(right + 1, value)

        def pointQuery(index):
            index += 1
            result = 0

            while index > 0:
                result ^= bit[index]
                index -= index & -index

            return result

        chars = list(s)
        answer = []

        # -----------------------------------
        # 4. Process queries
        # -----------------------------------

        for q in queries:

            parts = q.split()

            if parts[0] == "update":

                u = int(parts[1])
                newChar = parts[2]

                oldMask = charMask(chars[u])
                newMask = charMask(newChar)

                delta = oldMask ^ newMask

                # Every descendant root-path contains u
                left = tin[u]
                right = tin[u] + size[u] - 1

                rangeXor(left, right, delta)

                chars[u] = newChar

            else:

                u = int(parts[1])
                v = int(parts[2])

                w = lca(u, v)

                maskU = rootMask[u] ^ pointQuery(tin[u])
                maskV = rootMask[v] ^ pointQuery(tin[v])

                pathMask = (
                    maskU
                    ^ maskV
                    ^ charMask(chars[w])
                )

                answer.append(
                    pathMask.bit_count() <= 1
                )

        return answer