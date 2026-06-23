class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=len(nums)
        a=(s*(s+1)/2)
        b=0
        for i in nums:
            b+=i
        return int(a)-b