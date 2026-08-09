class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            prefix = 1 if i-1 < 0 else nums[i-1] * prefix
            product[i] *= prefix

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            postfix = 1 if i+1 > len(nums)-1 else nums[i+1] * postfix
            product[i] *= postfix

        return product
        