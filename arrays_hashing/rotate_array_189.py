class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def swap(left, right):
            while(left < right): 
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
            return nums

        if len(nums) <= 1:
            return nums
        
        k = k % len(nums)  #k should be < len(nums)
        print(swap(0, len(nums) - 1)) #reverse array
        print(swap(0, k - 1)) #sort k elements
        print(swap(k, len(nums) - 1)) #sort remaining elements
