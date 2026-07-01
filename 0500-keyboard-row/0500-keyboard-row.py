class Solution:
    def findWords(self, words: List[str]) -> List[str]:
       
        q="QWERTYUIOPqwertyuiop"
        a="ASDFGHJKLasdfghjkl"
        z="ZXCVBNMzxcvbnm"
        res=[]
        maxCount =0
        
        for i in words:
            qCount =0
            aCount =0
            zCount =0
            for ch in i:
                if ch in q:
                    qCount+=1
                elif ch in a:
                    aCount+=1
                else:
                    zCount+=1 
            maxCount = max(qCount,max(aCount,zCount))
            print(maxCount) 
               
            if len(i) ==  maxCount:
                res.append(i)
        return res              
