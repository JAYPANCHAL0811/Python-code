# 3.2 Stack Simulator
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack Underflow"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return "Stack is Empty"

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(f"Current Stack (Top -> Bottom): {self.items[::-1]}")


# Simulation
stack = Stack()
print("1. Pushing 5 items: 10, 20, 30, 40, 50")
for val in [10, 20, 30, 40, 50]:
    stack.push(val)

print(f"2. Peek top element: {stack.peek()}")

print(f"3. Popped element: {stack.pop()}")
print(f"   Popped element: {stack.pop()}")

print("4. Display stack state:")
stack.display()