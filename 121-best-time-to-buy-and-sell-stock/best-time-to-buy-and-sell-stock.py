class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxPrice = 0
        minCost = prices[0]
        for i in range(len(prices)):
            minCost = min(prices[i],minCost)
            if (i > 0):
                maxPrice = max((prices[i]-prices[i-1]), maxPrice)
                maxPrice = max(maxPrice, prices[i] - minCost)
        return maxPrice
        