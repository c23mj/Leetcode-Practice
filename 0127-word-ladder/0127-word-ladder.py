class Solution:
    def gen_adjacents(self, word: str) -> set:
        res = set()
        alph = 'abcdefghijklmnopqrstuvwxyz'
        for i in range(len(word)):
            for char in alph:
                res.add(word[:i] + char + word[i+1:])
        res.discard(word)
        return res

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set([word for word in wordList if len(word) == len(beginWord)])
        adjacents = defaultdict(set)
        if beginWord not in wordSet:
            adjacents[beginWord] = self.gen_adjacents(beginWord).intersection(wordSet)
        for word in wordSet:
            adjacents[word] = self.gen_adjacents(word).intersection(wordSet)

        frontier = deque([(beginWord, 1)])
        seen = set()
        while frontier:
            word, length = frontier.popleft()
            # print(f'word: {word}, length: {length}')
            adjs = adjacents[word] - seen
            if endWord in adjs:
                return length + 1
            seen.update(adjs)
            frontier.extend([(adj, length + 1) for adj in adjs])

        return 0
