class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for log in logs:
            if log == "../":
                depth = max(depth - 1, 0)
            elif log == "./":
                continue
            else:
                depth += 1
        return depth