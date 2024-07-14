class Solution:
    def numSteps(self, s: str) -> int:
        i = 0
        while s != "1":
            # print(s)
            if s[-1] == "0":
                s = s[:-1]
            else:
                s = str(bin(int(s, 2) + 1))[2:]
            i  = i + 1

        return i
