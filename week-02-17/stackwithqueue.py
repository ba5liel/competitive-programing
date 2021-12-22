class MyStack:
    stack: list = []
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(5)
# param_2 = obj.pop()
# param_3 = obj.top()
print(obj.stack)
param_4 = obj.empty()

print(param_4)