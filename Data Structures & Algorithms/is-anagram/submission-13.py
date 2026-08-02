class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counter_s = [0] * 26
        counter_t = [0] * 26

        for i in range(0, len(s)):
            counter_s[ord(s[i])-ord('a')] += 1
            counter_t[ord(t[i])-ord('a')] += 1
        
        return counter_s == counter_t
        