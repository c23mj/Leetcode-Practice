from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = Counter(arr)
        i = 0
        for word in arr:
            if ctr[word] == 1:
                i += 1
                if i == k:
                    return word
        return ''