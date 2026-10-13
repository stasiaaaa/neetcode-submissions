class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Time xomplexity: O(n)
        # Space complexity: O(1)
        lowest = prices[0]
        maxProfit = 0

        for price in prices:
            lowest = min(lowest, price)
            profit = price - lowest
            maxProfit = max(profit, maxProfit)

        return maxProfit
            
            
            

        