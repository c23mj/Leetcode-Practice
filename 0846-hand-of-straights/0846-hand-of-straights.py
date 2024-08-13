from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        cardCounts = Counter(hand)
        cards = sorted(cardCounts.keys())
        for val in cards:
            valCount = cardCounts[val]
            if valCount == 0:
                continue
            for i in range(groupSize):
                if cardCounts[val + i] < valCount:
                    return False
                cardCounts[val + i] -= valCount
        return True