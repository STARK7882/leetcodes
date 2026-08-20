class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        f={}
        for i in arr:
            f[i]=f.get(i,0)+1
        m=0
        for i in f.values():
            if(i>m):
                m=i
        for i,j in f.items():
            if(j==m):
                return i