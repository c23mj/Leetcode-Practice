from typing import Tuple
from collections import deque

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:

        def get_land(coord: Tuple[int, int]):
            far_right, far_down = coord[0], coord[1]
            while(far_right < len(land) and land[far_right][coord[1]]):
                far_right += 1
            while(far_down < len(land[0]) and land[coord[0]][far_down]):
                far_down += 1
            plot = [coord[0], coord[1], far_right-1, far_down-1]
            return plot
        
        groups = []
        for x in range(len(land)):
            for y in range(len(land[0])):
                if land[x][y] and (x == 0 or not land[x-1][y]) and (y == 0 or not land[x][y-1]):
                    groups.append(get_land((x, y)))
        return groups
        