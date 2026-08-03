class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        if head is None:
            return None

        if head.next is None:
            return TreeNode(head.val)

        slow = head
        fast = head
        prev = None

        while fast and fast.next:

            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        root = TreeNode(slow.val)

        root.left = self.sortedListToBST(head)

        root.right = self.sortedListToBST(slow.next)

        return root