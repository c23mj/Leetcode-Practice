from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counts = Counter(s1)
        # print(f"s1_counts: {s1_counts}")
        window_counts = Counter()
        n = len(s2)
        l, r = 0, 0
        while r < n:
            # print(f"loop start. window_counts: {window_counts}")
            while r < n and window_counts & s1_counts == window_counts:
                window_counts[s2[r]] += 1
                # print(f"incrementing. window_counts: {window_counts}")
                r += 1
                if window_counts == s1_counts:
                    return True
            while l < r and window_counts & s1_counts != window_counts:
                window_counts[s2[l]] -= 1
                # print(f"decrementing. window_counts: {window_counts}")

                l += 1
        return False
            