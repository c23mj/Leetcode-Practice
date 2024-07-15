class Solution:
    def firstUniqChar(self, s: str) -> int:
        for char in s:
            if s.rindex(char) == s.index(char):
                return s.index(char)
            
                
        return -1