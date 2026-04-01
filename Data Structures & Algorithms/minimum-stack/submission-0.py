class MinStack:

    def __init__(self):
        self.min_stack = []
        self.minimum = [] # minimum value at any given index
        self.length = 0

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if len(self.minimum) == 0:
            self.minimum.append(val)
        else:
            if val < self.minimum[-1]:
                self.minimum.append(val)
            else:
                self.minimum.append(self.minimum[-1])
        self.length += 1
        return

    def pop(self) -> None:
        self.min_stack.pop()
        self.minimum.pop()
        return

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1] if self.minimum else 0
