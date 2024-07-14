class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        empty, full = 0, numBottles
        drank = 0
        while full > 0:
            drank += full
            empty += full
            full, empty = divmod(empty, numExchange)
            
        return drank