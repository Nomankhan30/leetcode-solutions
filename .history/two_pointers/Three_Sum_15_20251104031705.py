from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  
        leny = len(nums)
        sumL = []
        
        for i in range(leny - 2):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate fixed elements
                continue
            
            current = i
            left = i + 1
            right = leny - 1
            
            while left < right:
                sumy = nums[current] + nums[left] + nums[right]
                
                if sumy == 0:
                    sumL.append([nums[current], nums[left], nums[right]])
                    
                    # Skip duplicate left values from being appended
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicate right values from being appended
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif sumy < 0:
                    left += 1
                else:
                    right -= 1
        
        return sumL


