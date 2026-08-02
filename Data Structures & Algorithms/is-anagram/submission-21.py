class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}

        for char_s in s:
            s_map[char_s] = s_map.get(char_s, 0) + 1
        
        for char_t in t:
            t_map[char_t] = t_map.get(char_t, 0) + 1

        return s_map == t_map