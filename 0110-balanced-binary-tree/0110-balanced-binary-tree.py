class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):

            if root is None:
                return 0

            l = height(root.left)

            r = height(root.right)

            return 1 + max(l,r)

        if root is None:
            return True

        l = height(root.left)

        r = height(root.right)

        if abs(l-r) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)