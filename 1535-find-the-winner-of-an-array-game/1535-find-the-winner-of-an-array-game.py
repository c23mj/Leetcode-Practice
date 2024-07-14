class Solution(object):
    def getWinner(self, arr, k):
        if k >= len(arr):
            return max(arr)
        if k == 1:
            return max(arr[0], arr[1])
        wins = 0
        while wins < k:
            # print(arr)
            if arr[0] > arr[1]:
                wins += 1
                arr.append(arr.pop(1))
            else:
                wins = 1
                arr.append(arr.pop(0))
        return arr[0]
            
        

        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        