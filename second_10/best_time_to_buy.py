class Solution(object):
    def maxProfit(self, prices):
        left = 0
        right = 1
        maxprof = 0
        for right in range(1,len(prices)):
            if(prices[left]>prices[right]):
                left = right
            if(prices[left]<prices[right]):
                if(maxprof < prices[right] - prices[left]):
                    maxprof = prices[right] - prices[left]
        return maxprof


