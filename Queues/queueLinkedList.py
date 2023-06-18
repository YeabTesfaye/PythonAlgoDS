class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.nodes = 0


class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __iter__(self):
        itr = self.linkedList.head
        while itr:
            yield itr.data
            itr = itr.next

    def __len__(self):
        return self.linkedList.nodes

    def is_empty(self) -> bool:
        return self.linkedList.head is None

    def enqueue(self, data) -> None:
        node = Node(data)
        if self.is_empty():
            self.linkedList.head = node
            self.linkedList.tail = node
        else:
            self.linkedList.tail.next = node
            self.linkedList.tail = node
        self.linkedList.nodes += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue.")

        first_value = self.linkedList.head.data

        if self.linkedList.head == self.linkedList.tail:
            self.linkedList.head = None
            self.linkedList.tail = None
        else:
            self.linkedList.head = self.linkedList.head.next

        self.linkedList.nodes -= 1
        return first_value

    def peek(self):
        if self.is_empty():
            raise IndexError("The Queue is empty.")
        return self.linkedList.head.data

    def clear(self):
        if not self.is_empty():
            self.linkedList = LinkedList()



#sample implemenentation 

# Create a new queue
queue = Queue()

# Enqueue elements
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

# Check if the queue is empty
print(queue.is_empty())  # Output: False

# Get the length of the queue
print(len(queue))  # Output: 3

# Dequeue elements
print(queue.dequeue())  # Output: 10
print(queue.dequeue())  # Output: 20

# Peek at the front of the queue
print(queue.peek())  # Output: 30

# Clear the queue
queue.clear()

# Check if the queue is empty after clearing
print(queue.is_empty())  # Output: True
