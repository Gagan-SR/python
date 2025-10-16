from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Fix the first element (i)
        for i in range(n - 3):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: Check for early exit or impossible scenarios
            # If the smallest possible sum (nums[i] + 3*nums[i+1]) is > target, no solution possible with this i
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target and nums[i] >= 0:
                # This early exit needs care with negative numbers and large targets
                # A safer optimization without worrying about overflow or signs:
                # If i is fixed, the smallest sum is nums[i] + nums[i+1] + nums[i+2] + nums[i+3]
                # The largest sum is nums[i] + nums[n-3] + nums[n-2] + nums[n-1]
                # If smallest > target or largest < target, we can prune, but the two-pointer naturally handles this.
                pass 

            # Step 3: Fix the second element (j)
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second element
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Step 4: Two Pointers for the remaining two elements
                left, right = j + 1, n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        ans.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move pointers and skip duplicates for the third and fourth elements
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif current_sum < target:
                        left += 1  # Need a larger sum, move left pointer right
                    else:
                        right -= 1 # Need a smaller sum, move right pointer left
                        
        return ans
