class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        n = 0
        for num in nums:
            n ^= num # gets you n1 xor n2

        unique_bit = n & -n
        # print(unique_bit)
        res = [0, 0]
        for num in nums:
            if(unique_bit & num) == 0:
                res[0] ^= num
            else:
                res[1] ^= num
        return res
    