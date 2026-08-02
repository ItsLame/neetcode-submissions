class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        
        for s in strs:
            count = len(s)
            encoded_str += f"{count}:{s}"

        print("encode?", encoded_str)

        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        
        i = 0
        while i < len(s) - 1:
            j = i

            while s[j] != ':':
                j += 1

            word_len = int(s[i:j])
            j += 1

            i = j + word_len
            word = s[j:i]
            print("###")
            print('how many?', word_len)
            print('from?', j)
            print('to?', i)
            print('word?', word)

            decoded_list.append(word)

        
        return decoded_list
