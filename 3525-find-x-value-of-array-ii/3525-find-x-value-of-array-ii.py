from typing import List

class Solution:
    def resultArray(
        self,
        nums: List[int],
        k: int,
        queries: List[List[int]]
    ) -> List[int]:

        n = len(nums)

        # Each tree node stores:
        # tree[node][0] = product of whole segment % k
        # tree[node][1] = counts of prefix-product remainders
        tree = [None] * (4 * n)

        def merge(left, right):
            if left is None:
                return right
            if right is None:
                return left

            left_prod, left_count = left
            right_prod, right_count = right

            count = left_count[:]

            # Prefix can contain the entire left segment
            # followed by a prefix of the right segment
            for r in range(k):
                new_r = (left_prod * r) % k
                count[new_r] += right_count[r]

            prod = (left_prod * right_prod) % k

            return (prod, count)

        def build(node, l, r):
            if l == r:
                value = nums[l] % k

                count = [0] * k
                count[value] = 1

                tree[node] = (value, count)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, value):
            if l == r:
                value %= k

                count = [0] * k
                count[value] = 1

                tree[node] = (value, count)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def query(node, l, r, ql, qr):
            if qr < l or r < ql:
                return None

            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            left = query(node * 2, l, mid, ql, qr)
            right = query(node * 2 + 1, mid + 1, r, ql, qr)

            return merge(left, right)

        build(1, 0, n - 1)

        answer = []

        for index, value, start, x in queries:

            # Update persists
            nums[index] = value
            update(1, 0, n - 1, index, value)

            # Consider nums[start ... n-1]
            prod, count = query(
                1, 0, n - 1,
                start, n - 1
            )

            answer.append(count[x])

        return answer