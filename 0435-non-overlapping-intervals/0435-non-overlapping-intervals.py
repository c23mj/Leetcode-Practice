class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        end_times = sorted(intervals, key = lambda x: x[1])
        curr_end, total_removed = float("-inf"), 0
        for interval in end_times:
            if curr_end > interval[0]:
                total_removed += 1
            else:
                curr_end = interval[1]
        return total_removed