class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        costs = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
        # print(costs)
        totalCost = 0
        back = 0
        best = 0
        for i in range(len(costs)):
            totalCost += costs[i]
            while totalCost > maxCost:
                totalCost -= costs[back]
                back += 1
            best = max(best, i - back + 1)

        return best
                
                


        return 0