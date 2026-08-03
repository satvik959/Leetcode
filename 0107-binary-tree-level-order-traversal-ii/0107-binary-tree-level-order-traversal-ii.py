from collections import deque

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([root])
        a = []

        while q:
            n = len(q)
            l = []

            for i in range(n):
                x = q.popleft()
                l.append(x.val)

                if x.left:
                    q.append(x.left)

                if x.right:
                    q.append(x.right)

            a.append(l)

        a.reverse()

        return a