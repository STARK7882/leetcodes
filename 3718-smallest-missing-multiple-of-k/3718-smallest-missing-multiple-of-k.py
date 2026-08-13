class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        a=k
        for i in range(len(nums)+1):
            if(a not in nums):
                return a
            a+=k