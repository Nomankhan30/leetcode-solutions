class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(1, len(prices)):
            #check if tommorow price is greater than today
            #so increase profit by selling stock
            #else dont sell stock
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
