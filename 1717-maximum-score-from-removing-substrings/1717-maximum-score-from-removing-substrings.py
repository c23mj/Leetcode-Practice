class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        bigger, smaller = max(x, y), min(x, y)
        best, other = ('ab', 'ba') if x == bigger else ('ba', 'ab')
        
        total_points = 0
        stack = []
        for char in s:
            if stack and stack[-1] == best[0] and char == best[1]:
                stack.pop()
                total_points += bigger
            else:
                stack.append(char)

        secondStack = []
        for char in stack:
            if secondStack and secondStack[-1] == other[0] and char == other[1]:
                secondStack.pop()
                total_points += smaller
            else:
                secondStack.append(char)
        return total_points

