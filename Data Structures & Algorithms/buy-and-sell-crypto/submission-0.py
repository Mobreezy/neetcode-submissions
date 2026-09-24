class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        out  = 0
        while s < len(prices):
            prof = prices[s] - prices[b]

            if prof > out:
                out = prof 

            if prices[b] > prices[s]:
                b+=1
                s= b+1
            else:
                s+=1
            
        return out
