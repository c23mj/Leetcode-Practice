class Solution:
    def numberOfSteps(self, num: int) -> int:
        i = 0
        while(num > 0):
            num = num / 2 if num % 2 == 0 else num - 1
            i += 1
        return i