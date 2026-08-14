class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort(key=lambda x:x[0])
        mgd=[intervals[0]]
        
        for c in intervals[1:]:
            l=mgd[-1]
            if l[1]>=c[0]:
                l[1]=max(l[1],c[1])
            else:
                mgd.append(c)
        return mgd