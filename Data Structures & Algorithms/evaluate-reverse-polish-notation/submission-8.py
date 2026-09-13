class Solution:
    def plus(self, a: int, b: int):
        return a + b

    def minus(self, a: int, b: int):
        return a - b

    def multiply(self, a: int, b: int):
        return a * b
    
    def divide (self, a: int, b: int):
        return a / b

    def isInt(self, val: str) -> bool:
        try:
            int(val)
            return True
        except:
            return False
    
    def isInt(self, val: str) -> bool:
        try:
            int(val)
            return True
        except:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for t in tokens:
            if self.isInt(t):
                nums.append(int(t))
            else:
                if t == "+":
                    nums[-2] = int(self.plus(nums[-2], nums[-1]))
                    nums.pop()
                elif t == "-":
                    nums[-2] = int(self.minus(nums[-2], nums[-1]))
                    nums.pop()
                elif t == "*":
                    nums[-2] = int(self.multiply(nums[-2], nums[-1]))
                    nums.pop()
                elif t == "/":
                    nums[-2] = int(self.divide(nums[-2], nums[-1]))
                    nums.pop()

        return int(nums[0])
