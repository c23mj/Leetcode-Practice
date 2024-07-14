class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sum_threshold = threshold * k
        running_sum = sum(arr[:k])
        out = 0
        if running_sum >= sum_threshold:
            out += 1
        for i in range(k, len(arr)):
            running_sum -= arr[i - k]
            running_sum += arr[i]
            if running_sum >= sum_threshold:
                out += 1
        return out