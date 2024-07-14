class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = 10 * num + digits[i]
        num += 1
        return [int(c) for c in str(num)]