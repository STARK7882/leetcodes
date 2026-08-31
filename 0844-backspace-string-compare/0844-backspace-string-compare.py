class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        l=[]
        k=[]
        for i in s:
            if i=="#":
                if not l:
                    continue
                else:
                    l.pop()
            else:
                l.append(i)
                
        for i in t:
            if i=="#":
                if not k:
                    continue
                else:
                    k.pop()
            else:
                k.append(i)
        return l==k














