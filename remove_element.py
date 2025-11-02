from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # 'write_idx' (the slow pointer) tracks the position where the next non-val element should be placed.
        # It also acts as the counter (k) for the number of elements not equal to 'val'.
        write_idx = 0
        
        # 'i' (the fast pointer) iterates through all elements of the array.
        for i in range(len(nums)):
            
            # Check if the current element is NOT the value we need to remove.
            if nums[i] != val:
                
                # This element is a keeper. Move it to the 'write_idx' position.
                nums[write_idx] = nums[i]
                
                # Advance the write pointer to the next available slot.
                write_idx += 1
                
            # If nums[i] == val, we simply skip the element and only increment 'i' (the loop takes care of this). 
            # This effectively "removes" the element by overwriting it later with a non-val element.
            
        # The final value of write_idx is the count (k) of elements that are not equal to 'val'.
        return write_idx
