class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMin = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)) :
            maxProfit = max(prices[i] - currMin, maxProfit)
            currMin = min(currMin, prices[i])
        
        return maxProfit
        