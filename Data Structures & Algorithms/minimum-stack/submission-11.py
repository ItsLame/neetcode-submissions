class MinStack:
    # stack = []
    # min_num = []
    # min_latest = float('inf')

    def __init__(self):
        self.stack = []
        self.min_num = []
        self.min_latest = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)


        if val < self.min_latest:
            self.min_latest = val

        self.min_num.append(self.min_latest)

    def pop(self) -> None:
        self.stack.pop()
        self.min_num.pop()

        if len(self.min_num) > 0:
            self.min_latest = self.min_num[-1]
        else:
            self.min_latest = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_num[-1]
