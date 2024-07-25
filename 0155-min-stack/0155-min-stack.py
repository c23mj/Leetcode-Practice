class MinStack:

    def __init__(self):
        self.minElement = float('inf')
        self.stack = []
        
        
    def push(self, val: int) -> None:
        self.minElement = min(self.minElement, val)
        self.stack.append({'val': val, 'min': self.minElement})

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minElement = self.stack[-1]['min']
        else:
            self.minElement = float("inf")
        
    def top(self) -> int:
        return self.stack[-1]['val']

    def getMin(self) -> int:
        return self.stack[-1]['min']
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()