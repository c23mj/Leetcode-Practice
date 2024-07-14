class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:        
        position.sort()
        # print(position)
        def checkPlacable(val: int):
            prev, count = position[0], 1
            for pos in position[1:]:
                if pos - prev >= val:
                    prev = pos
                    count += 1
            return count >= m


        l, r, res = 1, position[-1] - position[0], -1

        while l <= r:
            mid = (l + r) // 2
            if checkPlacable(mid):
                res = mid
                l = mid + 1
            else:
                r = mid - 1
        # return position[-1] - position[0]
        return res

