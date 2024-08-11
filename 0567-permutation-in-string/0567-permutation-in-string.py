from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        if len(s1) == len(s2):
            return Counter(s1) == Counter(s2)
        
        # sliding window
        s1_counts = Counter(s1)
        s2_counts = Counter()        
        l = r = 0
        while r < len(s2):
            while r < len(s2) and s2_counts & s1_counts == s2_counts:
                s2_counts[s2[r]] += 1
                r += 1
                if s2_counts == s1_counts:
                    return True
            while l < r and s2_counts & s1_counts != s2_counts:
                s2_counts[s2[l]] -= 1
                l += 1
        return False