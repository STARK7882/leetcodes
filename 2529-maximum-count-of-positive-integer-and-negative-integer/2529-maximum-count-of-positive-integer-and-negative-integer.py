class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        p=0
        n=0
        for i in nums:
            if 0<i:
                p+=1
            elif 0>i:
                n+=1
        return(max(n,p))
        