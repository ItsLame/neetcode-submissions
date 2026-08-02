class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = dict()
        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)

        return sorted(anagrams.values(), key=len)
        