class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # counter = dict()
        # for n in nums:
        #     counter[n] = counter.get(n, 0) + 1
        # return list(dict(sorted(counter.items(), reverse=True, key=lambda x: x[1])[:k]).keys())

        counter = dict({k:[] for k in range(len(nums) + 1)})
        uniq_nums = set(nums)
        for n in uniq_nums:
            counter[nums.count(n)].append(n)
        
        ans = []
        for i in range(len(nums), -1, -1):
            if len(counter[i]) == 0:
                continue

            for n in counter[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
        