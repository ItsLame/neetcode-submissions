class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = dict()

        for i in range(len(nums)):
            need = target - nums[i]
            if need in visited:
                return [visited[need], i]
            visited[nums[i]] = i

        return []
        