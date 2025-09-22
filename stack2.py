# Stack implementation using list
stack = []

# Push elements into stack
stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

# Pop elements from stack
print("Popped element:", stack.pop())
print("Stack after pop:", stack)

# Peek (see top element without removing)
print("Top element:", stack[-1])

# Check if stack is empty
if not stack:
    print("Stack is empty")
else:
    print("Stack is not empty")
