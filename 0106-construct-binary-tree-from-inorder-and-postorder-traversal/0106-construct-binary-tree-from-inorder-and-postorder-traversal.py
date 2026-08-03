class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:

        if not inorder or not postorder:
            return None

        x = postorder[-1]

        root = TreeNode(x)

        i = inorder.index(x)

        root.right = self.buildTree(
            inorder[i+1:],
            postorder[i:-1]
        )

        root.left = self.buildTree(
            inorder[:i],
            postorder[:i]
        )

        return root