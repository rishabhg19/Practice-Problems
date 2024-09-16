class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = -inf
        for right in range(1, len(prices)):
            maxProf = max(prices[right] - minPrice, maxProf)
            if prices[right] < minPrice:
                minPrice = prices[right]
        return max(maxProf, 0)
