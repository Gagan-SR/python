import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        
        # Min-Heap (Priority Queue)
        min_heap = []
        
        # A counter is used to break ties if two nodes have the same 'val'.
        # This is necessary because Python's heapq will raise a TypeError
        # if it tries to compare two ListNode objects with equal 'val'.
        counter = 0 
        
        # 1. Initialize the Heap with the head of every list
        for head in lists:
            if head:
                # Store as (value, counter, node)
                heapq.heappush(min_heap, (head.val, counter, head))
                counter += 1
        
        # 2. Initialize the merged list with a dummy node
        dummy = ListNode(0)
        current = dummy
        
        # 3. Build the merged list
        while min_heap:
            # Extract the smallest node from the heap
            # We only care about the node itself for the list construction
            val, _, min_node = heapq.heappop(min_heap)
            
            # Append the smallest node to the merged list
            current.next = min_node
            current = current.next
            
            # If the extracted node has a 'next' node, push it to the heap
            if min_node.next:
                heapq.heappush(min_heap, (min_node.next.val, counter, min_node.next))
                counter += 1
                
        # 4. Return the merged list (skip the dummy head)
        return dummy.next
