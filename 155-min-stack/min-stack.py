class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []

        self.maxInt = float('-inf')
        self.minInt = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.maxInt = max(self.maxInt, val)
        self.minInt = min(self.minInt, val)
        if (val <= self.minInt):
            self.minStack.append(val)
            self.minInt = self.minStack[-1]
        if (val >= self.maxInt):
            self.maxStack.append(val)
            self.maxInt = self.maxStack[-1]
           

    def pop(self) -> None:
        top = self.stack[-1]
        self.stack.pop()
        if top == self.maxInt:
            self.maxStack.pop()
            self.maxInt = self.maxStack[-1] if self.maxStack else float('-inf')
        if top == self.minInt: 
            self.minStack.pop()
            self.minInt = self.minStack[-1] if self.minStack else float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minInt


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()