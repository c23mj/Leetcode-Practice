class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
       gram_map = defaultdict(list)
       print(sorted(strs[0]))
       for s in strs:
            gram_map[str(sorted(s))].append(s)
       return list(gram_map.values())