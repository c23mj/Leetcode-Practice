class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = set(words[0])
        freq_maps = defaultdict(lambda: float("inf"))
        for word in words:
            curr = defaultdict(int)
            for char in word:
                if char in letters:
                    curr[char] += 1
            for letter in letters:
                freq_maps[letter] = min(freq_maps[letter], curr[letter])
        out = []
        for key in freq_maps.keys():
            for i in range(freq_maps[key]):
                out.append(key)

        return out

    