class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        st_counter = [0] * 26

        # 97 is ordinal value for lowercase 'a'
        for s_char in s:
            st_counter[ord(s_char) - 97] += 1
        
        for t_char in t:
            st_counter[ord(t_char) - 97] -= 1

        return st_counter == [0] * 26

        