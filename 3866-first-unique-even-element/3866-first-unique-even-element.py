class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        c=0
        for i in nums:
            if i%2==0 and nums.count(i)==1:
                c=i
                break
            else:
                c=-1
        return(c)