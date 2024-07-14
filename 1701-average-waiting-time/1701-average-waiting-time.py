class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        time, total, count = customers[0][0], 0, 0
        for customer in customers:
            time = max(time, customer[0])
            time += customer[1]
            total += time - customer[0]
            count += 1
        return total / float(count)