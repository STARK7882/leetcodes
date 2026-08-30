class Solution:
    def minOperations(self, logs: List[str]) -> int:
        l=[]
        for i in logs:
            if i=="../":
                if not l:
                    continue
                else:
                    l.pop()
            elif i=="./":
                continue
            else:
                l.append(i)
        return len(l)