class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0: return False
        freqs = defaultdict(int)
        for card in hand:
            freqs[card] += 1
        # print(freqs)
        keys = sorted(list(freqs.keys()), reverse=True)
        while keys:
            curr = keys[-1]
            # print(curr)
            for i in range(curr, curr + groupSize):
                if freqs[i] <= 0:
                    return False
                freqs[i] -= 1
            while keys and freqs[keys[-1]] == 0:
                keys.pop()
            # print(f"next round: {freqs}")
            # print(keys)

        return True


        