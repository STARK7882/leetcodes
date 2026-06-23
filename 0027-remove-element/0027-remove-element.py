class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        k=[]
        k.extend(nums)
        return (len(k))
