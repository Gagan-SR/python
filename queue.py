# Queue Implementation in Python

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue operation (insert at rear)
    def enqueue(self, item):
        self.queue.append(item)
        print(f"Enqueued: {item}")

    # Dequeue operation (remove from front)
    def dequeue(self):
        if not self.is_empty():
            removed = self.queue.pop(0)
            print(f"Dequeued: {removed}")
            return removed
        else:
            print("Queue is empty! Cannot dequeue.")

    # Peek operation (front element)
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty! No front element.")

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Display queue
    def display(self):
        print("Queue:", self.queue)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()

print("Front element:", q.peek
