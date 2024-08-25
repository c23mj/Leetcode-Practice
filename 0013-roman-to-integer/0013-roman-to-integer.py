class Solution:
    def romanToInt(self, s: str) -> int:
        romanToIntMap = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        lastVal = totalVal = 0
        for char in s[::-1]:
            nextVal = romanToIntMap[char]
            if nextVal < lastVal:
                totalVal -= nextVal
            else:
                totalVal += nextVal
            lastVal = nextVal
        return totalVal
            
            
        