from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        INF = float('inf')
        memo = {}

        def c(ind, rem):
            #base cases
            if rem == 0:
                return 0

            if rem < 0 or ind == len(coins):
                return INF

            key = (ind, rem)
            if key in memo:
                return memo[key]

            #including current coin in count
            take = 1 + c(ind, rem - coins[ind])

            #excluding current coin
            skip = c(ind + 1, rem)

            memo[key] = min(take, skip)
            return memo[key]

        ans = c(0, amount)
        #otherwise when amount is not made so INF will be written
        #which violates question constraints.
        return ans if ans != INF else -1
