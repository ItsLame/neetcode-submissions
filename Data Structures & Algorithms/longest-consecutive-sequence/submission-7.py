class Solution:
    def isStart(self, start: int, nums: List[int]) -> bool:
        if start - 1 not in nums:
            return True
        return False

    def countSequence(self, start: int, nums: List[int]) -> int:
        end = False
        
        latest = start
        counter = 1

        while end is False:
            if latest + 1 in nums:
                latest += 1
                counter += 1
            else:
                end = True

        return counter
    
    def longestConsecutive(self, nums: List[int]) -> int:
        longest_sequence = 0
        nums_set = set(nums)

        for num in nums_set:
            # 1. check whether it's a start of a sequence
            # 2. if not, skip. if yes, check for next item
            if self.isStart(num, nums_set):
                latest_sequence = self.countSequence(num, nums_set)
                if latest_sequence > longest_sequence:
                    longest_sequence = latest_sequence

        return longest_sequence