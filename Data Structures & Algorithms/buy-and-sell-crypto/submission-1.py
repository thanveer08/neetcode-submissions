class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == sorted(prices, reverse = True):
            return 0
        l = 0
        max_profit = 0
        for r in range (len (prices)):
            while prices[r] - prices[l] <0 :
                l = l+1
            max_profit = max(max_profit,prices[r] - prices[l] )      
        return max_profit        
