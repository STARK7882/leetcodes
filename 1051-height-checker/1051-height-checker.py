class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        l=[]
        for i in heights:
            l.append(i)
        l.sort()
        count=0
        for i in range(len(l)):
            if heights[i]!=l[i]:
                count+=1
        return count