from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if root is None:
            return []

        q = deque([root])

        ans = []

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

            ans.append(l)

        return ans