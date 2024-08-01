from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_len = len(s)
        if s_len < len(t):
            return ''
        t_count = Counter(t)
        s_count = Counter()
        min_l_r = (0, float('inf'))
        l, r = 0, 0
        while r < s_len:
            check = False
            while r < s_len and t_count & s_count != t_count:
                s_count[s[r]] += 1
                r += 1
            if t_count & s_count == t_count:
                check = True
            while l < r and t_count & s_count == t_count:
                s_count[s[l]] -= 1
                l += 1
            if check and r - l < min_l_r[1] - min_l_r[0]:
                min_l_r = (l, r)
    
            # print(f'found window: {s[l - 1: r]}')
        if min_l_r == (0, float('inf')):
            return ''
        return s[min_l_r[0] - 1: min_l_r[1]]