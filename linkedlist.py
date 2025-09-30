# Node class
class Node:
    def __init__(self, data):
        self.data = data   # store data
        self.next = None   # store reference to next node


# LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:   # if list is empty
            self.head = new_node
            return
        last = self.head
        while last.next:  # move to last node
            last = last.next
        last.next = new_node

    # Display the linked list
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Delete a node by value
    def delete(self, key):
        temp = self.head

        # If head node holds the key
        if temp and temp.data == key:
            self.head = temp.next
            temp = None
            return

        # Search for the key
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next

        if temp is None:  # key not found
            return

        prev.next = temp.next
        temp = None


# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()

ll.delete(20)
ll.display()
