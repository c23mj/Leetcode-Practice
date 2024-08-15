class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        netGas = [gas[i] - cost[i] for i in range(len(gas))]
        print(netGas)
        if sum(netGas) < 0:
            return -1
        idx, currSum = 0, 0
        for i in range(len(netGas)):
            currSum += netGas[i]
            if currSum < 0:
                currSum = 0
                idx = i + 1
        return idx