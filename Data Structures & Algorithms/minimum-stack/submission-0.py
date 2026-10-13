class MinStack:

    def __init__(self):
        self.ls=[]
        
        

    def push(self, val: int) -> None:
        self.ls.append(val)

    def pop(self) -> None:
        self.ls.pop()

    def top(self) -> int:
        return self.ls[-1]

    def getMin(self) -> int:
        return min(self.ls)
        
