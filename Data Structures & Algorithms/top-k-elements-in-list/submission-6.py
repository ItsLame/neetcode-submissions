class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = dict()

        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1

        print('dict', nums_dict)

        nums_heap = []
        for key, n in nums_dict.items():
            heapq.heappush(nums_heap, [n*-1, key])
        
        print('heap', nums_heap)

        k_ans = []
        for _ in range(k):
            ans = heapq.heappop(nums_heap)
            print('pop?', ans)
            k_ans.append(ans[1])

        print('ans', k_ans)

        return k_ans