class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        r = 1
        maxProfit = 0

        while (r < len(prices)) :
            if prices[l] < prices[r] :
                profit = prices[r] - prices[l]
                print(profit)
                maxProfit = max(maxProfit, profit)
            else :
                l = r
            r = r + 1
        
        return maxProfit

        