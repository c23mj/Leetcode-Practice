class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        cols, posDiags, negDiags = set(), set(), set()
        board = [['.' for i in range(n)] for j in range(n)]
        res = []
        def backtrack(r: int):
            if r == n:
                res.append([''.join(row) for row in board])
            for c in range(n):
                posDiag, negDiag = r + c, r - c
                
                if c not in cols and posDiag not in posDiags and negDiag not in negDiags:
                    board[r][c] = 'Q'
                    cols.add(c)
                    posDiags.add(posDiag)
                    negDiags.add(negDiag)
                    
                    backtrack(r + 1)
                    
                    board[r][c] = '.'
                    cols.remove(c)
                    posDiags.remove(posDiag)
                    negDiags.remove(negDiag)
        backtrack(0)
        return res
                    
                
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         cols, posDiag, negDiag = set(), set(), set()
#         res = []
#         board = [['.' for i in range(n)] for j in range(n)]

#         def backtrack(r):
#             if r == n:
#                 res.append([''.join(row) for row in board])
#             for c in range(n):
#                 if c not in cols and r + c not in posDiag and r - c not in negDiag:
#                     board[r][c] = 'Q'
#                     cols.add(c)
#                     posDiag.add(r + c)
#                     negDiag.add(r - c)

#                     backtrack(r + 1)

#                     board[r][c] = '.'
#                     cols.remove(c)
#                     posDiag.remove(r + c)
#                     negDiag.remove(r - c)
#         backtrack(0)
#         return res




