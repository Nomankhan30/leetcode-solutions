from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for ind in range(0, len(nums)):
            if nums[ind] not in dic:
                dic[nums[ind]] = ind
            else:
                i1 = dic[nums[ind]]
                i2 = ind
                if abs(i1 - i2) <= k:
                    return True
                dic[nums[ind]] = ind  
        return False
