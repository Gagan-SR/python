class Queue:
    def __init__(self):
        self.items = []

    # Add an element to the queue
    def enqueue(self, item):
        self.items.append(item)
        print(f"{item} added to the queue.")

    # Remove an element from the queue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty! Cannot dequeue.")
            return None
        removed_item = self.items.pop(0)
        print(f"{removed_item} removed from the queue.")
        return removed_item

    # Check if the queue is empty
    def is_empty(self):
        return len(self.items) == 0

    # Display the elements of the queue
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue:", self.items)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()
