from collections import deque
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = []
        queue = deque(range(1, 10))
        while queue:
            n = queue.popleft()
            if n > high:
                break
            if low <= n <= high:
                res.append(n)
            if n % 10 < 9:
                queue.append(n * 10 + n % 10 + 1)
        return res