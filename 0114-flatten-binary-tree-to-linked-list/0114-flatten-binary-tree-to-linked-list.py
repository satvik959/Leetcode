class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:

        if root is None:
            return

        self.flatten(root.left)

        self.flatten(root.right)

        t = root.right

        root.right = root.left

        root.left = None

        x = root

        while x.right:
            x = x.right

        x.right = t