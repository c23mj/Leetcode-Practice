class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        out = []
        for i in range(len(temperatures) - 1, -1, -1):
            currVal = temperatures[i]
            while stack:
                val, idx = stack[-1]
                if currVal < val:
                    out.append(idx - i)
                    break
                else:
                    stack.pop()
            if not stack:
                out.append(0)
            stack.append((currVal, i))
        return out[::-1]
            

