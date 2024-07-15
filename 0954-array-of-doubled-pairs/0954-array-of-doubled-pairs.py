class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        map = defaultdict(int)
        seen_without = False
        for i in range(len(arr)):
            map[arr[i]] += 1

        while True:
            if len(arr) == 1:
                return not seen_without
            if len(arr) == 0:
                return True
            if arr[0] > 0:
                if map[arr[0] * 2] > 0:
                    map[arr[0]] -= 1
                    map[arr[0] * 2] -= 1
                    arr.remove(arr[0] * 2)
                    arr.pop(0)
                else:
                    if seen_without:
                        return False
                    else:
                        seen_without = True
                        arr.remove(arr[0])

            else:
                if map[arr[0] / 2] > 0:
                    map[arr[0]] -= 1
                    map[arr[0]/2] -= 1
                    arr.remove(arr[0]/2)
                    arr.pop(0)
                else:
                    if seen_without:
                        return False
                    else:
                        seen_without = True
                        arr.remove(arr[0])



                    


            

            

        