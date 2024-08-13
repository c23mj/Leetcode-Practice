class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        t_chars = set(t)
        s = [char if char in t_chars else '' for char in s]
        memo = [[0 for i in range(len(s))] for j in range(len(t))]
        
        # base case
        first_count = 0
        for i in range(len(s)):
            if s[i] == t[0]:
                first_count += 1
            memo[0][i] = first_count
            
        for j in range(1, len(t)):
            for i in range(1, len(s)):
                memo[j][i] += memo[j][i - 1]
                if t[j] == s[i]:
                    memo[j][i] += memo[j - 1][i -1]
                    
        return memo[-1][-1]
            
          
                
                
        
        
        