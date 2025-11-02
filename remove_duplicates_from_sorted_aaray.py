from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Edge case for an empty array
        if not nums:
            return 0
        
        # 'k' is the pointer for the next position to insert a unique element (the "write" pointer)
        # It also represents the count of unique elements found so far.
        k = 1 
        
        # 'i' is the pointer to iterate through the array (the "read" pointer), starting from the second element
        for i in range(1, len(nums)):
            
            # Compare the current element (nums[i]) with the previous element (nums[i-1]).
            # Since the array is sorted, we only need to compare adjacent elements.
            if nums[i] != nums[i - 1]:
                
                # Found a new unique element.
                # 1. Move the unique element to the 'k' position.
                nums[k] = nums[i]
                
                # 2. Increment 'k' to point to the next available spot for a unique element.
                k += 1
                
            # If nums[i] == nums[i-1], it is a duplicate, so we just increment 'i' (continue the loop) 
            # and effectively skip/ignore the duplicate, leaving 'k' unchanged.
            
        # 'k' now holds the count of unique elements (which is the new length)
        return k
