class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        tmp = ''
        n = len(s)
        for i in range(n//2):
            tmp = s[n - 1 - i]
            s[n-1-i] = s[i]
            s[i] = tmp
            