class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) == 0:
            return 0
        profit, lowValue = 0, prices[0]
        for price in prices:
            if price<lowValue:
                lowValue = price
            if price>lowValue:
                profit = profit + price - lowValue
                lowValue = price
        return profit