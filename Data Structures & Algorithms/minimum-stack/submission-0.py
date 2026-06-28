class MinStack:
    # sol:
    # step1
    # define 2 stacks 
    # one holds the stack and the other holds 
    # the minimum value of the stack
    def __init__(self):
        self.stack = []
        # the smallest will always be on top
        self.minstack = []
        

    def push(self, val: int) -> None:
        # step2
        # what happens when you push to a stack?
        # Hint: what function do you use to push 
        # to a stack?...append
        self.stack.append(val)
        # step3.
        # choose the smallest between the 2
        # we want to make sure we keep track of the minimum
        val = min(val, self.minstack[-1] if self.minstack else val)
        self.minstack.append(val)

    def pop(self) -> None:
        # step 4 pop from both
        self.stack.pop()
        self.minstack.pop()        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
