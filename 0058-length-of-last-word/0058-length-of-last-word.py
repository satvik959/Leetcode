class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        l = s.split()
        output=len(l[-1])
        return output
        
