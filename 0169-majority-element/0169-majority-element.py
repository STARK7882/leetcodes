from collections import Counter as c
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        a=c(nums)
        print(a)
        return max(a, key=a.get)