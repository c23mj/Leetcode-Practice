class Solution(object):
    def findKthPositive(self, arr, k):
        present = set(arr)
        i, count = 0, 0
        while count < k:
            i += 1
            if i not in present:
                count += 1
        return i
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        