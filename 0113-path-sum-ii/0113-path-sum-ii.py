class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:

        ans = []

        def dfs(root, target, path):

            if root is None:
                return

            path.append(root.val)

            target -= root.val

            if root.left is None and root.right is None:

                if target == 0:
                    ans.append(path[:])

            dfs(root.left, target, path)

            dfs(root.right, target, path)

            path.pop()

        dfs(root, targetSum, [])

        return ans