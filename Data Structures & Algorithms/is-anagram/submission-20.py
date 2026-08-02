class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_counter = {}
        t_counter = {}

        # 1 loop -> O(n)
        # 2nd loop -> O(n)
        # complexity 2 O(n)

        for s_char in s:
            s_counter[ord(s_char)] = s_counter.get(ord(s_char), 0) + 1

        for t_char in t:
            t_counter[ord(t_char)] = t_counter.get(ord(t_char), 0) + 1

        return s_counter == t_counter
            