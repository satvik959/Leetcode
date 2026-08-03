class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        if not preorder or not inorder:
            return None

        x = preorder[0]

        root = TreeNode(x)

        i = inorder.index(x)

        root.left = self.buildTree(
            preorder[1:i+1],
            inorder[:i]
        )

        root.right = self.buildTree(
            preorder[i+1:],
            inorder[i+1:]
        )

        return root