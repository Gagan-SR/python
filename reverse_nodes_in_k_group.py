# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        # Helper function to reverse a standard linked list segment
        def reverse_list(head_node: ListNode) -> ListNode:
            prev = None
            curr = head_node
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            # 'prev' will be the new head
            return prev

        # 1. Create a dummy node to handle the new head easily
        dummy = ListNode(0)
        dummy.next = head
        
        # 'prev_group_tail' tracks the end of the previously reversed group
        prev_group_tail = dummy
        
        while True:
            # 2. Check if k nodes remain
            # 'kth_node' will point to the k-th node in the current segment
            kth_node = prev_group_tail
            for _ in range(k):
                kth_node = kth_node.next
                if not kth_node:
                    # Not enough nodes left, stop and return the result
                    return dummy.next

            # 3. Identify the start and end of the segment to be reversed
            group_head = prev_group_tail.next  # Start of the k-group
            next_group_head = kth_node.next   # Start of the next group (node after kth_node)

            # 4. Temporarily detach and reverse the k-group
            kth_node.next = None  # Cut the k-group from the rest of the list
            
            # The 'new_head' is the result of the standard list reversal
            new_head = reverse_list(group_head) 

            # 5. Reconnect the reversed group to the list
            
            # Connect the tail of the *previous* group to the *new head* of the current reversed group
            prev_group_tail.next = new_head
            
            # The original 'group_head' is now the *tail* of the reversed group.
            # Connect this new tail to the head of the *next* group.
            group_head.next = next_group_head

            # 6. Prepare for the next iteration
            # 'prev_group_tail' must now be the tail of the *just-reversed* group (which is the original group_head)
            prev_group_tail = group_head
