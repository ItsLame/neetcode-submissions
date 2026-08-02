class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numsUniq = set(nums)
        if (len(nums) != len(numsUniq)):
            return True
        else:
            return False
         