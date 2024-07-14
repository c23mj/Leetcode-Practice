class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefixes = defaultdict(int)
        currTotal = 0
        for el in nums:
            currTotal += el
            prefixes[currTotal % k] += 1

        # print(prefixes)
        out = 0
        for count in prefixes.values():
            if count > 1:
                out += math.comb(count, 2)
        out += prefixes[0]
        return out