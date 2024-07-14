class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if len(s) == 0:
            return [[]]
        if len(s) == 1:
            return [[s]]
        out = []
        curr = ""
        for i in range(len(s)):
            curr = curr + s[i]
            if curr == curr[::-1]:
                out.extend([[curr] + sub_partition for sub_partition in self.partition(s[i+1:])])
        return out

