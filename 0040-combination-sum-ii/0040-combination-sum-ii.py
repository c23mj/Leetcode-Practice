class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        print(candidates)
        memo = dict()
        def combHelper(target: int, i: int) -> List[List[int]]:
            # print(f"calling combHelper on {target}, {i}")
            if target == 0:
                return [[]]
            if (target, i) in memo:
                return memo[(target, i)]
            out = []
            unique = set()
            for j in range(i, len(candidates)):
                if candidates[j] > target:
                    break
                cands = [[candidates[j]] + comb for comb in combHelper(target - candidates[j], j + 1)]
                for cand in cands:
                    if tuple(cand) not in unique:
                        unique.add(tuple(cand))
                        out.append(cand)
            memo[(target, i)] = out
            # print(f"output: {out}")
            return out
        return combHelper(target, 0)

