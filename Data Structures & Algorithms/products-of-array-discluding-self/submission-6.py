class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            # approach 1: retrieve the previous index
            # prefix = 1 if i-1 < 0 else nums[i-1] * prefix
            # product[i] *= prefix

            # approach 2: multiply before the next loop
            product[i] *= prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            # postfix = 1 if i+1 > len(nums)-1 else nums[i+1] * postfix
            # product[i] *= postfix

            product[i] *= postfix
            postfix *= nums[i]

        return product
        