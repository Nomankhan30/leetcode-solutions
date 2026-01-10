from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)

        def dfs(i):
            if i == n:
                return 0

            if i in memo:
                return memo[i]

            # must include nums[i]
            memo[i] = nums[i] + max(0, dfs(i + 1))
            return memo[i]

        ans = nums[0]
        for i in range(n):
            ans = max(ans, dfs(i))

        return ans
