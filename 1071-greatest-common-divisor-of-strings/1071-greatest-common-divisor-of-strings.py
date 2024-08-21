class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isRepeated(s: str, t: str) -> bool:
            if len(s) % len(t) != 0:
                return False
            n = len(s) // len(t)
            return s == t * n
            
        if len(str1) < len(str2):
            str1, str2 = str2, str1
        for i in range(len(str1), 0, -1):
            substr = str1[:i]
            if isRepeated(str1, substr) and isRepeated(str2, substr):
                return substr
        return ''
        