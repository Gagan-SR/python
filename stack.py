# Stack Implementation in Python

class Stack:
    def __init__(self):
        self.stack = []

    # Push operation
    def push(self, item):
        self.stack.append(item)
        print(f"Pushed: {item}")

    # Pop operation
    def pop(self):
        if not self.is_empty():
            removed = self.stack.pop()
            print(f"Popped: {removed}")
            return removed
        else:
            print("Stack is empty! Cannot pop.")

    # Peek operation (top element)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is empty! No top element.")

    # Check if stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Display stack
    def display(self):
        print("Stack:", self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()

print("Top element:", s.peek())
s.pop()
s.display()
