from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = Counter(arr)
        distinct = set(word for word in ctr if ctr[word] == 1)
        if len(distinct) < k:
            return ''
        i = 0
        for word in arr:
            if word in distinct:
                i += 1
                if i == k:
                    return word
        