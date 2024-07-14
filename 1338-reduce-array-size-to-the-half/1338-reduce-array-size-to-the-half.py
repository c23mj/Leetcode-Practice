class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        occurences = defaultdict(int)
        for el in arr:
            occurences[el] += 1

        lst = sorted(occurences.values(), reverse=True)
        removed = 0
        arr_len = len(arr)/2 if len(arr) % 2 == 0 else len(arr)/2 + 1
        for i in range(len(lst)):
            removed += lst[i]
            if removed >= arr_len:
                return i + 1
        