class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        i = 0
        for num_1 in nums:
            difference = target - num_1
            j = 0
            for num_2 in nums:
                if num_2 == difference and i != j:
                    return [i, j]
                j += 1
            i += 1