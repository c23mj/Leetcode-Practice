class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        if minutes > len(customers):
            return sum(customers)
        unsatisfied = [customers[i] if grumpy[i] else 0 for i in range(len(customers))]
        curr = sum(unsatisfied[:minutes])
        best, totalUnsatisfied = curr, curr
        # print(unsatisfied)
        for i in range(minutes, len(unsatisfied)):
            totalUnsatisfied += unsatisfied[i]
            curr += unsatisfied[i] - unsatisfied[i - minutes]
            best = max(best, curr)
        return sum(customers) + best - totalUnsatisfied
        