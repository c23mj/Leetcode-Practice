from collections import deque
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        seen = set(['0000'])
        # print(seen)
        if '0000' in deads: return -1
        def getAdjs(combo: str):
            adjs = []
            for i in range(4):
                upOne = combo[0:i] + (str((int(combo[i]) + 1) % 10)) \
                        + combo[i+1:]
                downOne = combo[0:i] + (str((int(combo[i]) + 9) % 10)) \
                        + combo[i+1:]
                if upOne not in deads and upOne not in seen: 
                    seen.add(upOne)
                    adjs.append(upOne)
                if downOne not in deads and downOne not in seen:
                    seen.add(downOne)
                    adjs.append(downOne)
            return adjs

        frontier = deque([('0000', 0)])
        while frontier:
            currCombo, currDepth = frontier[0]
            frontier.popleft()
            # print(f"currCombo: {currCombo}, currDepth: {currDepth}")
            if currCombo == target: 
                return currDepth
            adjacents = [(adjCombo, currDepth + 1) for adjCombo in getAdjs(currCombo)]
            frontier.extend(adjacents)
            
        return -1
        
                

        
        