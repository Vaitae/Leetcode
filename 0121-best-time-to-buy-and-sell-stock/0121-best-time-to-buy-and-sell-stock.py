class Solution(object):
    def maxProfit(self, prices):
        maxP=0
        l,r=0,1

        while r<len(prices):
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP, profit)
            else:
                l=r
            r+=1
        return maxP

        