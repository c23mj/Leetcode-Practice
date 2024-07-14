class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        relative_locs = defaultdict(lambda: -1)
        for i in range(len(arr2)):
            item = arr2[i]
            if item not in relative_locs:
                relative_locs[item] = len(relative_locs)
    

        out = [[] for _ in range(len(relative_locs) + 1)]
        for item in arr1:
            out[relative_locs[item]].append(item)
        
        out[-1].sort()

        return [item for sublist in out for item in sublist]
