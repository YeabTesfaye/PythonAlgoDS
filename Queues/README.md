# Queue

A queue is a linear data structure that follows the "first in, first out" (FIFO) principle. It allows for the ordered storage and retrieval of elements. Similar to people waiting in a queue, the first element added to the queue is the first one to be removed. Queues are commonly used in various applications such as job scheduling, request handling, and data processing.

## Time and Space Complexity

For the Queue data structure, the time and space complexity can vary based on the underlying implementation. Here's a comparison of the time and space complexity for the Queue List and Queue Linked List implementations:

### Queue List

| Method        | Description                               | Time Complexity        | Space Complexity     |
|---------------|-------------------------------------------|------------------------|----------------------|
| `enqueue`     | Adds an element to the end of the queue    | O(1)                   | O(1)                 |
| `dequeue`     | Removes and returns the front element      | O(n)                   | O(1)                 |
| `peek`        | Returns the front element without removing | O(1)                   | O(1)                 |
| `is_empty`    | Checks if the queue is empty               | O(1)                   | O(1)                 |
| `clear`       | Removes all elements from the queue        | O(1)                   | O(1)                 |
| `__len__`     | Returns the number of elements in the queue| O(1)                   | O(1)                 |
| `__iter__`    | Iterates over the elements in the queue    | O(n)                   | O(1)                 |

### Queue Linked List

| Method        | Description                               | Time Complexity        | Space Complexity     |
|---------------|-------------------------------------------|------------------------|----------------------|
| `enqueue`     | Adds an element to the end of the queue    | O(1)                   | O(1)                 |
| `dequeue`     | Removes and returns the front element      | O(1)                   | O(1)                 |
| `peek`        | Returns the front element without removing | O(1)                   | O(1)                 |
| `is_empty`    | Checks if the queue is empty               | O(1)                   | O(1)                 |
| `clear`       | Removes all elements from the queue        | O(1)                   | O(1)                 |
| `__len__`     | Returns the number of elements in the queue| O(1)                   | O(1)                 |
| `__iter__`    | Iterates over the elements in the queue    | O(n)                   | O(1)                 |



Note: n is the number of elements in the queue.

