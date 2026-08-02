class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = dict()
        for n in nums:
            counter[n] = counter.get(n, 0) + 1
        return list(dict(sorted(counter.items(), reverse=True, key=lambda x: x[1])[:k]).keys())

        # counter = dict()
        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        # ans = []
        # for i in range(k):
        #     ans.append(counter.pop(max(counter)))
        # return ans