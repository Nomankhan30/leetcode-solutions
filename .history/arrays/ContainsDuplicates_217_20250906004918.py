class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for num in nums:
            if num not in dic:
                dic[num]=False
            else: #if num appears twice
                return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.containsDuplicate([1, 2, 3, 1]))   # expected True
    print(sol.containsDuplicate([1, 2, 3, 4]))   # expected False