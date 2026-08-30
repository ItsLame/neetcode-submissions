class Solution:
    def isValid(self, s: str) -> bool:
        opening_brackets = []

        if len(s) <= 1:
            return False

        for c in s:
            if c in "{[(":
                opening_brackets.append(c)
                continue
            else:
                if len(opening_brackets) == 0:
                    return False

            if opening_brackets:
                if c == "}" and opening_brackets[-1] != "{":
                    return False
                if c == "]" and opening_brackets[-1] != "[":
                    return False
                if c == ")" and opening_brackets[-1] != "(":
                    return False
                opening_brackets.pop()

        if len(opening_brackets) == 0:
            return True
        else:
            return False