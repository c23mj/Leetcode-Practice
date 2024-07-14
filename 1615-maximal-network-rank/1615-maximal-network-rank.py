from collections import defaultdict
class Solution(object):
    def maximalNetworkRank(self, n, roads):
        adjs = defaultdict(set)
        for road in roads:  
            adjs[road[0]].add(road[1])
            adjs[road[1]].add(road[0])  

        maxRank = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                maxRank = max(maxRank, len(adjs[i]) + len(adjs[j]) if j not in adjs[i] else len(adjs[i]) + len(adjs[j]) - 1)
        return maxRank

        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        """
        