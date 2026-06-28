class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c={}
        r=0
        mxc=0
        for i in nums:
            c[i]=c.get(i,0)+1
            if c[i] > mxc:
                r=i
            mxc=max(c[i],mxc)
        return r