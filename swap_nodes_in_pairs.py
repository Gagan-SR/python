# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: If the list is empty or has only one node, no swap is needed.
        if not head or not head.next:
            return head

        # Nodes to be swapped (1st and 2nd in the current pair)
        first_node = head
        second_node = head.next

        # Recursively process the rest of the list starting from the 3rd node (second_node.next)
        # This will be the new head of the rest of the list after it's swapped.
        remaining_list = self.swapPairs(second_node.next)

        # 1. Attach the swapped remainder to the first node (which is now the second in the pair)
        first_node.next = remaining_list
        
        # 2. Complete the swap by making the second node point to the first node
        second_node.next = first_node

        # The second node is now the new head of this pair (and thus the new head for this subproblem)
        return second_node
