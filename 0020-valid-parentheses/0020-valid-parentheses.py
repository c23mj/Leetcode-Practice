class Solution:
    def isValid(self, s: str) -> bool:
        matchingBrackets = {')': '(', '}': '{', ']': '['}
        stack = []
        for char in s:
            if char in matchingBrackets:
                if not stack or matchingBrackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack