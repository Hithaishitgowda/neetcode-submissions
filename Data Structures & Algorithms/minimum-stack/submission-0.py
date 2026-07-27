class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            curr_val = val
            if curr_val < self.min_stack[-1]:
                self.min_stack.append(curr_val)
            else:
                self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        top = self.stack[len(self.stack)-1]
        return top

    def getMin(self) -> int:
        return self.min_stack[-1]

