class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

# Example Usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())    # Output: 30
print(s.peek())   # Output: 20
print(s.size())   # Output: 2
print(s.is_empty())  # Output: False

