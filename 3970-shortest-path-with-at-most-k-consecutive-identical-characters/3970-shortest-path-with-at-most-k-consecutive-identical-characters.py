from typing import List
import heapq

class Solution:
    def shortestPath(
        self,
        n: int,
        edges: List[List[int]],
        labels: str,
        k: int
    ) -> int:

        graph = [[] for _ in range(n)]

        for u, v, w in edges:
            graph[u].append((v, w))

        INF = float('inf')

        # dist[node][streak]
        dist = [[INF] * (k + 1) for _ in range(n)]

        # At node 0, its label appears once
        dist[0][1] = 0

        pq = [(0, 0, 1)]
        # (distance, node, streak)

        while pq:
            cost, u, streak = heapq.heappop(pq)

            if cost != dist[u][streak]:
                continue

            if u == n - 1:
                return cost

            for v, weight in graph[u]:

                if labels[v] == labels[u]:
                    new_streak = streak + 1
                else:
                    new_streak = 1

                # More than k consecutive identical characters
                if new_streak > k:
                    continue

                new_cost = cost + weight

                if new_cost < dist[v][new_streak]:
                    dist[v][new_streak] = new_cost

                    heapq.heappush(
                        pq,
                        (new_cost, v, new_streak)
                    )

        return -1