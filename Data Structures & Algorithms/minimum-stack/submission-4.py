class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = [math.inf]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum.append(min(self.minimum[-1], val))

    def pop(self) -> None:
        # last = self.stack[-1]
        # self.stack = self.stack[:-1]
        # return last
        self.minimum.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]
