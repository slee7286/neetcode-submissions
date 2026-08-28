class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for right in range(len(prices)):
            for left in range(0,right):
                if prices[right] - prices[left] > max:
                    max = prices[right] - prices[left]
        return max
            