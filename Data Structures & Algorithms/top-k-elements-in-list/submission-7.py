class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. count the number's quantity
        nums_count = dict()
        for n in nums:
            nums_count[n] = nums_count.get(n, 0) + 1

        # 2. use heap to sort
        nums_heap = []
        for key, value in nums_count.items():
            heapq.heappush(nums_heap, (value * -1, key))

        # print(nums_heap)

        # 3. pop to get k nums
        k_ans = []
        for _ in range(k):
            k_candidate = heapq.heappop(nums_heap)
            k_ans.append(k_candidate[1])

        return k_ans
        
