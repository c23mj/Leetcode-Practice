class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(nums):
            if len(nums) > 1:
                half = len(nums) // 2
                first_half = nums[:half]
                second_half = nums[half:]
                mergeSort(first_half)
                mergeSort(second_half)
                i, j, k = 0, 0, 0
                while i < len(first_half) and j < len(second_half):
                    if first_half[i] < second_half[j]:
                        nums[k] = first_half[i]
                        i += 1
                    else:
                        nums[k] = second_half[j]
                        j += 1
                    k += 1      
                while i < len(first_half):
                    nums[k] = first_half[i]
                    i += 1
                    k += 1
                         
                while j < len(second_half):
                    nums[k] = second_half[j]
                    j += 1
                    k += 1
                        
                
        mergeSort(nums)
        return nums