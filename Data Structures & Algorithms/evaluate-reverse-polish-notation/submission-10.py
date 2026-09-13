class Solution:
    def plus(self, a: int, b: int) -> int:
        return int(a + b)

    def minus(self, a: int, b: int) -> int:
        return int(a - b)

    def multiply(self, a: int, b: int) -> int:
        return int(a * b)
    
    def divide (self, a: int, b: int) -> int:
        return int(a / b)

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

        ops = {
            "+": self.plus,
            "-": self.minus,
            "*": self.multiply,
            "/": self.divide,
        }

        for t in tokens:
            if self.isInt(t):
                nums.append(int(t))
            else:
                func = ops.get(t)
                nums[-2] = func(nums[-2], nums[-1])
                nums.pop()

        return int(nums[0])
