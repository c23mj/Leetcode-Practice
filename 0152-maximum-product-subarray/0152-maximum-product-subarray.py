class Solution:
    def maxProdHelper(self, arr: List[int]):
        max_prod = min_prod = res = arr[0]
        for el in arr[1:]:
            if el < 0:
                max_prod, min_prod = min_prod, max_prod
            max_prod = max(el, el * max_prod)
            min_prod = min(el, el * min_prod)
            res = max(res, max_prod)
        return res

    def maxProduct(self, nums: List[int]) -> int:
        subArrays = [[]]
        for num in nums:
            if num == 0:
                subArrays.append([])
            else:
                subArrays[-1].append(num)
        maxSub = max((self.maxProdHelper(sub) for sub in subArrays if sub), default=float('-inf'))
        if len(subArrays) > 1:
            maxSub = max(maxSub, 0)
        return maxSub
