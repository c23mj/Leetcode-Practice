class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = sorted(score, reverse=True)
        lookupDict = {sortedScores[i]: i for i in range(len(sortedScores))}        
        # print(lookupDict)
        output = []
        for s in score:
            place = lookupDict[s] + 1
            if place > 3:
                output.append(str(place))
            elif place == 1:
                output.append("Gold Medal")
            elif place == 2:
                output.append("Silver Medal")
            else:
                output.append("Bronze Medal")
        return output