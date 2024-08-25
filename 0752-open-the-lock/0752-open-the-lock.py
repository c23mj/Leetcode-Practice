class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deads = set(deadends)
        if '0000' in deads:
            return -1
        seen = {'0000'}
        def adjs(combo: str) -> List[str]:
            validAdjs = []
            for i in range(4):
                currDigit = int(combo[i])
                upOne = combo[:i] + str((currDigit + 1) % 10) + combo[i+1:]
                downOne = combo[:i] + str((currDigit - 1) % 10) + combo[i+1:]
                for adj in [upOne, downOne]:
                    if adj not in seen and adj not in deads:
                        seen.add(adj)
                        validAdjs.append(adj)
            return validAdjs
        frontier = deque([('0000', 0)])
        while frontier:
            combo, cost = frontier.popleft()
            if combo == target:
                return cost
            frontier.extend([(c, cost + 1) for c in adjs(combo)])
        return -1
        
            
        
                
                