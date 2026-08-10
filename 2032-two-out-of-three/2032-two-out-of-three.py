class Solution:
    def twoOutOfThree(self, n1: List[int], n2: List[int], n3: List[int]) -> List[int]:
        s=[]
        for i in n1:
            if i in n2 or i in n3:
                s.append(i)
        for k in n2:
            if k in n1 or k in n3 and k not in s:
                s.append(k)
        for l in n3:
            if l in n1 or l in n2 and l not in s:
                s.append(l)
        d=set(s)
        return(list(d))