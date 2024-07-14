class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if not s1:
            return s2 == s3

        if not s2:
            return s1 == s3

        s1_len, s2_len, s3_len = len(s1), len(s2), len(s3)

        if s3_len != s1_len + s2_len:
            return False

        memo = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        memo[0][0] = True
        for i in range(1, s3_len + 1):
            for r in range(i + 1):
                c = i - r
                if c > s1_len:
                    continue
                if r > s2_len:
                    break 
                # print(f"i:{i} r:{r} c:{c}")       
                memo[r][c] = (r > 0 and s3[i - 1] == s2[r - 1] and memo[r-1][c]) or (c > 0 and s3[i - 1] == s1[c - 1] and memo[r][c-1])

        # print(memo)
        return memo[s2_len][s1_len]