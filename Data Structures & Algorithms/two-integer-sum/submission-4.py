class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i, v in enumerate(nums):
            # target = x + y
            # y = target - x
            # x is v

            y = target - v

            if y in nums_dict:
                return [nums_dict[y], i]
            else:
                nums_dict[v] = i

        return [0, 0]
        