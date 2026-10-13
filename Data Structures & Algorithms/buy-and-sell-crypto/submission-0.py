class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum=0
        for i in range(len(prices)):
            for j in range(i+1,len(prices)):
                ans=prices[j]-prices[i]
                if ans>0:
                    maximum=max(maximum,ans)
        return maximum

        