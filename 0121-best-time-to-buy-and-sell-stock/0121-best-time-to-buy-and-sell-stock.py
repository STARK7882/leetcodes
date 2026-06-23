class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        prof=0
        minpri=prices[0]
        for i in range(1,n):
            if prices[i]>minpri:
                prof=max(prof,prices[i]-minpri)
            else:
                minpri=prices[i]
        return prof