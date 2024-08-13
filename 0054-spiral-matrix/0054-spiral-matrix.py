class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        order = []
        while l <= r or t <= b:
            for i in range(l, r + 1):
                order.append(matrix[t][i])
            t += 1
            if t > b:
                break

            for j in range(t, b + 1):
                order.append(matrix[j][r])
            r -= 1
            
            if r < l:
                break

            for i in range(r, l - 1, -1):
                order.append(matrix[b][i])
            b -= 1
            if b < t:
                break

            for j in range(b, t - 1, - 1):
                order.append(matrix[j][l])    
            l += 1
            if l > r:
                break

        return order
                