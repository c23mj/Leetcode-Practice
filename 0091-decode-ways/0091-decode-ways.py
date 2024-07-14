class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        memo = [0] * (n + 1)
        memo[0] = 1
        memo[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                if s[i - 1] == '1' or s[i - 1] == '2':
                    memo[i + 1] = memo[i - 1]
                else:
                    return 0
            else:
                if s[i - 1] == '1' or s[i - 1] == '2' and int(s[i]) < 7:
                    memo[i + 1] += memo[i - 1]
                memo[i + 1] += memo[i]
        # print(memo)
        return memo[n]