class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        g=True
        for i in range(len(nums)-1):
            if nums[i]>=nums[i+1]:
                g=True
            else:
                g=False
                break
        if g==True:
            return True
        else:
            for j in range(len(nums)-1):
                if nums[j]<=nums[j+1]:
                    g=True
                else:
                    g=False
                    break
        return g