class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        # min = 0
        if len(self.stack) != 0 and self.min_stack[-1] < val:
            self.stack.append(val)
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
            self.stack.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if len(self.stack) == 0:
            return 0
        return self.stack[-1]
        
        
    def isEmpty(self) -> int:
        if len(self.stack) == 0:
            return 0
        return len(self.stack)
    
    def getMin(self) -> int:
        return self.min_stack[-1]