class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n=len(s)
        m=len(t)
        if n==0:
            return True
        if n>m:
            return False
        idx=0
        for i in range(m):
            if t[i]==s[idx]:
                idx+=1
            if idx==n:
                return True
        return idx==n