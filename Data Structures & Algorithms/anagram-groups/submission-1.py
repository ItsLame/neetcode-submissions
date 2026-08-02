class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # anagrams = dict()
        # for s in strs:
        #     sorted_s = "".join(sorted(s))
        #     if sorted_s not in anagrams:
        #         anagrams[sorted_s] = []
        #     if sorted_s in anagrams:
        #         anagrams[sorted_s].append(s)

        # return sorted(anagrams.values(), key=len)
        
        anagrams = dict()
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            
            key = tuple(counter)
            if key not in anagrams:
                anagrams[key] = []
            if key in anagrams:
                anagrams[key].append(s)

        return sorted(anagrams.values(), key=len)
