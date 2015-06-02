
class MinStack:
    # @param x, an integer
    # @return an integer
    def __init__(self):
        self.stack = []
        self.minValue = []
    
    def push(self, x):
        self.stack.append(x)
        if self.minValue and x<self.minValue[-1]:
            self.minValue.append(x)
        elif not self.minValue:
            self.minValue.append(x)
        else:
            self.minValue.append(self.minValue[-1])

    # @return nothing
    def pop(self):
        self.stack.pop()
        self.minValue.pop()

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.minValue[-1]
        