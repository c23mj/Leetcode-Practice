class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        # print(nums)
        pairs = []
        for i, val in enumerate(nums):
            # print(f"i at {i}. val: {val}")
            if val > 0:
                break
            if i > 0 and val == nums[i-1]:
                continue
                
            j, k = i + 1, len(nums) - 1
            while j < k:
                curr_sum = val + nums[j] + nums[k]
                # print(f"j, k, sum: {j}, {k}, {curr_sum}")
                if curr_sum < 0:
                    j += 1
                elif curr_sum > 0:
                    k -= 1
                else:
                    pairs.append([val, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                
            
        return pairs
            