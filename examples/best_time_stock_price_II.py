class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit += prices[i] - prices[i - 1]

        return max_profit

s = Solution()
prices = [7,1,5,3,6,4]
print(s.maxProfit(prices)) # Output, should be 7

ss = Solution()
prices = [1,2,3,4,5]
print(ss.maxProfit(prices)) # Output, should be 4

sss = Solution()
prices = [7,6,4,3,1]
print(sss.maxProfit(prices)) # Output, should be 0