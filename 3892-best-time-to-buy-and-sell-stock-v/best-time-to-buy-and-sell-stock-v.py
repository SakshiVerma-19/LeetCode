class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        if n < 2 or k == 0:
            return 0
        
    
        dp = [[0] * n for _ in range(k + 1)]
        
        for i in range(1, k + 1):
           
            max_buy = -prices[0]
            max_short = prices[0]
            
            for j in range(1, n):
                
                dp[i][j] = max(dp[i][j-1], prices[j] + max_buy, -prices[j] + max_short)
                
                if j < n - 1: 
                    max_buy = max(max_buy, dp[i-1][j-1] - prices[j])
                    max_short = max(max_short, dp[i-1][j-1] + prices[j])
                    
        return dp[k][n-1]