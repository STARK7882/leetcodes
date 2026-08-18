class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while(True):
            m=1
            for i in str(n):
                m*=int(i)
            if m%t==0:
                return n
            n+=1