class Solution:
    numbers = [str(i) for i in range(2, 10)]
    letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    def letterCombinations(self, digits: str) -> List[str]:
        combination_dict = {self.numbers[i]: self.letters[i] for i in range(8)}
        if digits == '': 
            return []
        combos = list(combination_dict[digits[0]])
        if len(digits) == 1:
            return combos
        # print(combos)
        return [l + suffix for l in combos for suffix in self.letterCombinations(digits[1:])]
