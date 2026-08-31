class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        criticals = []
        index = 1
        prev = head
        curr = head.next

        while curr and curr.next:
            # local maxima or local minima
            if (curr.val > prev.val and curr.val > curr.next.val) or \
               (curr.val < prev.val and curr.val < curr.next.val):
                criticals.append(index)

            prev = curr
            curr = curr.next
            index += 1

        # fewer than 2 critical points
        if len(criticals) < 2:
            return [-1, -1]

        # max distance = last - first
        max_dist = criticals[-1] - criticals[0]

        # min distance = min of consecutive differences
        min_dist = min(criticals[i+1] - criticals[i] for i in range(len(criticals)-1))

        return [min_dist, max_dist]
