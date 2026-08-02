class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_counter = dict()
        t_counter = dict()
        for i in range(len(s)):
            s_count = s_counter.get(s[i], 0)
            s_counter[s[i]] = s_count + 1

            t_count = t_counter.get(t[i], 0)
            t_counter[t[i]] = t_count + 1

        return s_counter == t_counter