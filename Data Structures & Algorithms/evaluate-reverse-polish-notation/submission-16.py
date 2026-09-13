class Solution:
    def plus(self, a: int, b: int) -> int:
        return int(a + b)

    def minus(self, a: int, b: int) -> int:
        return int(a - b)

    def multiply(self, a: int, b: int) -> int:
        return int(a * b)
    
    def divide (self, a: int, b: int) -> int:
        return int(a / b)

    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        ops = {
            "+": self.plus,
            "-": self.minus,
            "*": self.multiply,
            "/": self.divide,
        }

        for t in tokens:
            if ops.get(t, None) is not None:
                func = ops.get(t)
                nums[-2] = func(nums[-2], nums[-1])
                nums.pop()
            else:
                nums.append(int(t))

        return nums[0]
