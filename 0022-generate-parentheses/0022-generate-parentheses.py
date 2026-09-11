class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def f(l,r,s):
            if len(s)==n*2:
                res.append(s)
                return
            if l<n:
                f(l+1,r,s+"(")
        
            if r<l:
                f(l,r+1,s+")")
        
        res=[]
        f(0,0,"")
        return res