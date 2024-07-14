from collections import defaultdict
class Solution(object):
    def isAnagram(self, s, t):
        s_dict, t_dict = defaultdict(int), defaultdict(int) 
        for char in s:
            s_dict[char] += 1
        for char in t:
            t_dict[char] += 1
        
        for char in set(s + t):
            if s_dict[char] != t_dict[char]:
                return False

        return True
        