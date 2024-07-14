class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        edgeCounts = defaultdict(int)
        for road in roads:
            edgeCounts[road[0]] += 1
            edgeCounts[road[1]] += 1
        
        totals = sorted(list(edgeCounts.values()))
        totals = [0] * (n - len(totals)) + totals
        # print(totals)
        out = 0
        for i in range(1, n + 1):
            out += i * totals[i - 1]
        return out
