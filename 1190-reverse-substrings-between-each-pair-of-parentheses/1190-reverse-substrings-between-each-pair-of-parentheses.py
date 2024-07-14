class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        pair = dict()
        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                pair_left = stack.pop()
                pair[pair_left] = i
                pair[i] = pair_left
        res = []
        i = 0
        dx = 1
        while i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                dx = -dx
            else:
                res.append(s[i])
            i += dx
        return ''.join(res)
        
