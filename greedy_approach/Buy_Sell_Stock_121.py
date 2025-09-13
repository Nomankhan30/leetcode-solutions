from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPrice = prices[0]   
        maxProfit = 0          
        for i in range(1, len(prices)):
            # check profit if selling today
            profit = prices[i] - buyPrice

            # update max profit
            if profit > maxProfit:
                maxProfit = profit

            # update buy price if today is cheaper
            if prices[i] < buyPrice:
                buyPrice = prices[i]

        return maxProfit

        