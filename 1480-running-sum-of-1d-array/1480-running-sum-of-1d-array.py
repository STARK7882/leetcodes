class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        d=[]
        c=0
        for i in nums:
            c+=i
            d.append(c)
        return(d)