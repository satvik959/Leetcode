class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def check(a, b):

            if a is None and b is None:
                return True

            if a is None or b is None:
                return False

            if a.val != b.val:
                return False

            return check(a.left, b.right) and check(a.right, b.left)

        return check(root.left, root.right)