
class Queue:
    def __init__(self):
        self.list = []
        self.count = 0

    def __iter__(self):
        for value in self.list:
            yield value

    def __len__(self):
        return self.count

    def is_empty(self) -> bool:
        return self.count == 0

    def enqueue(self, value) -> None:
        self.list.append(value)
        self.count += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Remove from empty queue is not allowed.")

        remove = self.list.pop(0)
        self.count -= 1
        return remove
    def peek(self):
        if self.is_empty():
            raise IndexError("The Queue is empty.")
        return self.list[0]
    
    def reverse(self):
        self.list.reverse()
    
    def copy(self):
        copied_queue = Queue()
        copied_queue.list = self.list[:]
        copied_queue.count = self.count
        return copied_queue
    def get_all_elements(self):
        return self.list[:]
    
    def merege(self,queue):
        if not isinstance(queue,Queue):
            raise TypeError("Merege Operation requires Queue Object")
        self.list += queue.list
        self.count += queue.count
    def remove(self,value):
        self.list = [x for x in self.list if x != value]
        self.count = len(self.list)
    def clear(self) -> None:
        if not self.is_empty():
            self.list = []
            self.count = 0



