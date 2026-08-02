class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hash = dict()

        for i, n in enumerate(nums):
            num_to_find = target - n
            
            if num_to_find in nums_hash:
                return [nums_hash[num_to_find], i]
            
            nums_hash[n] = i

        return [0] 
            