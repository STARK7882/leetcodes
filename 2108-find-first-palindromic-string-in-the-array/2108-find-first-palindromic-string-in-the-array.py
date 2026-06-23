class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        n=""
        for i in words:
            if i==i[::-1]:
                n=i
                break
            else:
                n=""
        return n