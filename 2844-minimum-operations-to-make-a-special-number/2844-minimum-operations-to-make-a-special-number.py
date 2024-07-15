class Solution:
    def minimumOperations(self, num: str) -> int:
        n = len(num) 
        if n== 1:
            return 1 if num != '0' else 0
        five, zero = num.rfind('5'), num.rfind('0')
        best = float('inf')
        for i in range(zero - 1, -1, -1):
            if num[i] == '5' or num[i] == '0':
                print(i)
                best = min(best, n - i - 2)
                break
        for i in range(five - 1, -1, -1):
            if num[i] == '2' or num[i] == '7':
                print(i)
                best = min(best, n- i - 2)
                break
        if zero > -1:
            best = min(n - 1, best)
        else:
            best = min(n, best)
        return best
            
            
                
                