from typing import List
import heapq

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = []
        busy = []

        for i, weight in enumerate(servers):
            heapq.heappush(free, (weight, i))

        ans = []
        time = 0

        for i, task in enumerate(tasks):
            time = max(time, i)

            # Free all servers that have finished by current time
            while busy and busy[0][0] <= time:
                finish, weight, index = heapq.heappop(busy)
                heapq.heappush(free, (weight, index))

            # If no server is free, jump to the earliest finish time
            if not free:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    finish, weight, index = heapq.heappop(busy)
                    heapq.heappush(free, (weight, index))

            # Pick smallest weight, then smallest index
            weight, index = heapq.heappop(free)

            ans.append(index)

            # Server becomes busy until time + task
            heapq.heappush(
                busy,
                (time + task, weight, index)
            )

        return ans