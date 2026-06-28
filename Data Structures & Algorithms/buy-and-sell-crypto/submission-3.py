class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        maxPrice = 0
        for price in prices:
            if price < lowest:
                lowest = price
            maxPrice = max(maxPrice,price - lowest)
        return maxPrice