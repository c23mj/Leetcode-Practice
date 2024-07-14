class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervalDict = dict()
        for i in range(len(s)):
            if s[i] not in intervalDict:
                intervalDict[s[i]] = [i, i]
            else:
                intervalDict[s[i]][1] = i
        
        intervals = sorted(list(intervalDict.values()))
        out = []
        prev = intervals[0]
        for interval in intervals[1:]:
            if interval[0] <= prev[1]:
                prev[1] = max(prev[1], interval[1])
            else:
                out.append(prev[1] - prev[0] + 1)
                prev = interval
        out.append(prev[1] - prev[0] + 1)
        return out