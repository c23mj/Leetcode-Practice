class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m, n = len(board), len(board[0])    
        searched = set()
        def bfs(r: int, c: int):
            ### adj logic
            seen = {(r, c)}
            d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            def get_adjs(r: int, c: int):
                validAdjs = []
                containsEdge = (r == 0 or c == 0 or r == m - 1 or c == n - 1)
                for dx, dy in d:
                    a, b = r + dx, c + dy
                    if 0 <= a < m and 0 <= b < n and (a, b) not in seen and board[a][b] == 'O':
                        seen.add((a, b))
                        validAdjs.append((a, b))
                        if a == 0 or b == 0 or a == m - 1 or b == n - 1:
                            containsEdge = True
                return validAdjs, containsEdge
            ######
            frontier = deque([(r, c)])
            containsEdge = False
            while frontier:
                a, b = frontier.popleft()
                adjs, edgeInAdj = get_adjs(a, b)
                containsEdge |= edgeInAdj
                frontier.extend(adjs)
                
            searched.update(seen)
            if not containsEdge:
                for a, b in seen:
                    board[a][b] = 'X'
                    
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O' and (i, j) not in searched:
                    bfs(i, j)
            
        
            
            
                
                
            
            
            
        
        
        
        
        
        
        
        
        
        """
        Do not return anything, modify board in-place instead.
        """
        