class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s=set(nums)
        nums=list(s)
        print(nums)
        
        if len(nums)==3:
            return(min(nums))
        elif len(nums)<3:
            return(max(nums))
        elif len(nums)>3:
            nums.remove(max(nums))
            nums.remove(max(nums))
            return(max(nums))