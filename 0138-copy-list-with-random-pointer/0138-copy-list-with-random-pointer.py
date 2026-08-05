class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        oldToNew = {}

        cur = head
        while cur:
            oldToNew[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            oldToNew[cur].next = oldToNew.get(cur.next)
            oldToNew[cur].random = oldToNew.get(cur.random)
            cur = cur.next

        return oldToNew[head]