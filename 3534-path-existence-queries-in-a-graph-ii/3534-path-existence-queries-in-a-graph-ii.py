class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        a = sorted((nums[i], i) for i in range(n))

        v = [0] * n
        p = [0] * n

        for i in range(n):
            v[i] = a[i][0]
            p[a[i][1]] = i

        r = [0] * n
        j = 0

        for i in range(n):
            j = max(j, i)

            while j + 1 < n and v[j + 1] - v[i] <= maxDiff:
                j += 1

            r[i] = j

        c = [0] * n

        for i in range(1, n):
            c[i] = c[i - 1]

            if v[i] - v[i - 1] > maxDiff:
                c[i] += 1

        k = n.bit_length()
        b = [r]

        for x in range(1, k):
            t = [0] * n

            for i in range(n):
                t[i] = b[x - 1][b[x - 1][i]]

            b.append(t)

        ans = []

        for x, y in queries:
            l = p[x]
            h = p[y]

            if l > h:
                l, h = h, l

            if l == h:
                ans.append(0)
                continue

            if c[l] != c[h]:
                ans.append(-1)
                continue

            d = 0
            x = l

            for i in range(k - 1, -1, -1):
                if b[i][x] < h:
                    x = b[i][x]
                    d += 1 << i

            ans.append(d + 1)

        return ans