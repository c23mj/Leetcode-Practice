class Solution:
    def scoreOfString(self, s: str) -> int:
        total = 0
        curr = ord(s[0])
        for i in range(1, len(s)):
            nextval = ord(s[i])
            total += abs(curr - nextval)
            curr = nextval
        return total