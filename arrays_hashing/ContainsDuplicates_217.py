from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=False
            else: #if num appears twice
                return True
        return False

