class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for i in prices:
            maxP = max(i - minBuy, maxP)
            minBuy = min(minBuy, i)
        return maxP