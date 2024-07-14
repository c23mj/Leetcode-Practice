from collections import defaultdict
class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        memo = [defaultdict(lambda: float('inf'), {0: 0})]
        ringLookup = defaultdict(list)
        for i in range(len(ring)):
            ringLookup[ring[i]].append(i)

        for i in range(len(key)):
            nextCosts = defaultdict(lambda: float('inf'))
            for idx in ringLookup[key[i]]:
                for source in memo[i].keys():
                    cDist = (source - idx + len(ring)) % len(ring)
                    ccDist = len(ring) - cDist
                    bestDist = min(cDist, ccDist) + memo[i][source]
                    nextCosts[idx] = min(nextCosts[idx], bestDist)
            memo.append(nextCosts)
        return min(memo[len(key)].values()) + len(key)

