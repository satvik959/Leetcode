from typing import List
import heapq

class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:

        # Segment tree:
        # 1 = at least one free server exists in this range
        size = 1
        while size < k:
            size *= 2

        tree = [0] * (2 * size)

        # Initially every server is free
        for i in range(k):
            tree[size + i] = 1

        for i in range(size - 1, 0, -1):
            tree[i] = tree[2 * i] + tree[2 * i + 1]

        def update(index, value):
            pos = size + index
            tree[pos] = value
            pos //= 2

            while pos:
                tree[pos] = tree[2 * pos] + tree[2 * pos + 1]
                pos //= 2

        def find_first(start):
            # Find first free server >= start

            def search(node, left, right):
                if right < start or tree[node] == 0:
                    return -1

                if left == right:
                    return left if left < k else -1

                mid = (left + right) // 2

                ans = search(node * 2, left, mid)

                if ans != -1:
                    return ans

                return search(node * 2 + 1, mid + 1, right)

            return search(1, 0, size - 1)

        busy = []
        count = [0] * k

        for i in range(len(arrival)):
            time = arrival[i]

            # Free servers whose work has finished
            while busy and busy[0][0] <= time:
                finish, server = heapq.heappop(busy)
                update(server, 1)

            # No server available
            if tree[1] == 0:
                continue

            start = i % k

            server = find_first(start)

            # Wrap around
            if server == -1:
                server = find_first(0)

            # Assign request
            count[server] += 1

            update(server, 0)

            finish_time = time + load[i]

            heapq.heappush(
                busy,
                (finish_time, server)
            )

        maximum = max(count)

        return [
            i for i in range(k)
            if count[i] == maximum
        ]