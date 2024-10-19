class Solution(object):
    def maxProfit(self, prices):
        min_price = 100001
        profit = 0

        for price in prices:
            if price < min_price:
                min_price = price
            elif price - min_price > profit:
                profit = price - min_price

        return profit

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices)) # Output, should be 5

ss = Solution()
prices = [7,6,4,3,1]
print(ss.maxProfit(prices)) # Output, should be 0