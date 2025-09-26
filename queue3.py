# Queue implementation using list
queue = []

# Enqueue (adding elements)
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueue:", queue)

# Dequeue (removing elements)
print("Dequeued element:", queue.pop(0))
print("Queue after dequeue:", queue)
