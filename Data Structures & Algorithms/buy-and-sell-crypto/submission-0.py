class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        profit = 0

        for r in range(1, len(prices)):
            if prices[l] < prices[r]:
                p = prices[r] - prices[l]
                profit = max(profit, p)
            else:
                l = r
            
            r += 1
        
        return profit

            
