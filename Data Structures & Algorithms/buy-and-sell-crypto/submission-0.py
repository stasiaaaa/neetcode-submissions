class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # need to find biggest difference
        # constraint: ordered in days, can't buy/sell earlier
        
        # brute force, compare each element with each other, save difference
        profit = []

        for i, buy_price in enumerate(prices):
            for j, sell_price in enumerate(prices[i:]):
                profit_value = sell_price - buy_price
                profit.append(profit_value)
                
        return max(profit)
            
            
            

        