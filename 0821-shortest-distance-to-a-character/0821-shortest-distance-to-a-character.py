class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        k=[]
        r=[]
        for i in range(len(s)):
            if s[i]==c:
                k.append(i)
        for i in range(len(s)):
            if s[i]!=c:
                r.append(min(abs((i-j))for j in k))
            else:
                r.append(0)
        return r