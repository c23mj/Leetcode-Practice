class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        billCount = defaultdict(int)
        for bill in bills:
            billCount[bill] += 1
            if bill > 5:
                if billCount[5] == 0:
                    return False
                billCount[5] -= 1
                if bill == 20:
                    if billCount[10] > 0:
                        billCount[10] -= 1 
                    elif billCount[5] >= 2:
                        billCount[5] -= 2
                    else:
                        return False
        return True
           