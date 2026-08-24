class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        l=[]
        for i in bulbs:
            if bulbs.count(i)%2!=0 and i not in l:
                l.append(i)
        l.sort()
        return l