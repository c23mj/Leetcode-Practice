class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        start, end = intervals[0]
        for interval in intervals[1:]:
            if end >= interval[0]:
                end = max(end, interval[1])
            else:
                out.append([start, end])
                start, end = interval
        return out + [[start, end]]