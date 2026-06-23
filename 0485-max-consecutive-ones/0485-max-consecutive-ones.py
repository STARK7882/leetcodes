class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        mx=0
        r=0
        for i in nums:
            if i==1:
                r+=1
                mx=max(mx,r)
            else:
                r=0
        return mx