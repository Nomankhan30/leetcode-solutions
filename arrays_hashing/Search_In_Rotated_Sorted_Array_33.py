class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        mid = (left + right) // 2
        while (left <= right):
            mid = (left + right) // 2
            if nums[mid] == target: return mid

            # if left is sorted then check if target is in that part
            if (nums[left] <= nums[mid]):
                if (target >= nums[left] and target < nums[mid]):
                    right = mid - 1  # narrow down arr from end if target < nums[mid]
                else:
                    left = mid + 1  # target not in this array, move to right one

            # else right one is sorted
            elif target > nums[mid] and target <= nums[right]:  # check if in right array
                left = mid + 1  # if target > nums[mid] move forward
            else:  # narrow down search, squeeze end
                right = mid - 1

        # if target not found
        return -1
