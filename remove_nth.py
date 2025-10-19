# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        # Create a dummy node pointing to head (handles edge cases)
        dummy = ListNode(0)
        dummy.next = head
        
        first = dummy
        second = dummy
        
        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        
        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next
        
        # Delete the nth node
        second.next = second.next.next
        
        return dummy.next
