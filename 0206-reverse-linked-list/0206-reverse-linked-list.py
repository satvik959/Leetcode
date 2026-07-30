class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            # Save the next node
            next_temp = curr.next
            
            # Reverse the pointer
            curr.next = prev
            
            # Move prev and curr one step forward
            prev = curr
            curr = next_temp
        
        # prev is now at the old last node (new head)
        return prev
