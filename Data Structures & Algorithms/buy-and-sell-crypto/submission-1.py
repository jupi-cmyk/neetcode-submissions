class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local_min = 0
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i] - prices[local_min])
            if prices[i] < prices[local_min]:
                local_min = i
        return max_profit