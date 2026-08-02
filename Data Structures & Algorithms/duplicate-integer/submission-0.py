class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         processed = []
         for n in nums:
            if n in processed:
                return True
            processed.append(n)
         return False