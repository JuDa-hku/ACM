class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        maxEarn, minivalueNow = 0, prices[0]
        for price in prices:
            if price>minivalueNow:
                maxEarn = max(maxEarn, price-minivalueNow)
            else:
                minivalueNow = price
        return maxEarn
        