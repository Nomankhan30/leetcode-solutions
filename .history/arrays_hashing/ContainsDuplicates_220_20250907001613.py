from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        window = SortedList()
        for i, num in enumerate(nums):
            pos1 = window.bisect_left(num - valueDiff)
            if pos1 < len(window) and abs(window[pos1] - num) <= valueDiff:
                return True

            window.add(num)
            if len(window) > indexDiff:
                # remove oldest element to maintain sliding window of size indexDiff
                window.remove(nums[i - indexDiff])

        return False
