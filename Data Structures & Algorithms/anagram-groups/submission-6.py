class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = dict()

        for s in strs:
            word_array = [0] * 26

            for char in s:
                word_array[ord(char) - ord('a')] = word_array[ord(char) - ord('a')] + 1
            
            key = tuple(word_array)
            current_value = str_dict.get(key, [])
            current_value.append(s)
            str_dict[key] = current_value

        return list(str_dict.values())