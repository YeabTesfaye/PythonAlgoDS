
# Hash Table

A hash table, also known as a hash map, is a data structure that provides efficient storage and retrieval of key-value pairs. It uses a hash function to compute an index for each key, allowing for constant-time average-case lookup, insertion, and deletion operations. Hash tables are widely used for data storage and retrieval tasks, such as database indexing, caching, and symbol tables.

| Method              | Description                                                          | Time Complexity | Space Complexity |
|---------------------|----------------------------------------------------------------------|-----------------|------------------|
| `insert(key, value)` | Inserts a key-value pair into the hash table.                        | O(1)           | O(1)             |
| `find(key)`         | Retrieves the value associated with the given key from the hash table.| O(1)            | O(1)             |
| `update(key, value)`| Updates the value associated with the given key in the hash table.    | O(1)            | O(1)             |
| `delete(key)`       | Removes the key-value pair with the given key from the hash table.    | O(1)            | O(1)             |
| `list_all()`        | Returns a list of all values in the hash table.                       | O(n)            | O(n)             |

# BasicHashTable

The BasicHashTable is a hash table implementation that uses a simple array to store key-value pairs. It calculates the index using a hash function and stores the key-value pair at that index.

| Method              | Description                                                          | Time Complexity | Space Complexity |
|---------------------|----------------------------------------------------------------------|-----------------|------------------|
| `insert(key, value)` | Inserts a key-value pair into the hash table.                         | O(1)          | O(1)            |
| `find(key)`         | Retrieves the value associated with the given key from the hash table.| O(1)            | O(1)             |
| `update(key, value)`| Updates the value associated with the given key in the hash table.    | O(1)            | O(1)             |
| `delete(key)`       | Removes the key-value pair with the given key from the hash table.    | O(1)            | O(1)             |
| `list_all()`        | Returns a list of all values in the hash table.                       | O(n)            | O(n)             |

# ProbingHashTable

The ProbingHashTable is a hash table implementation that uses linear probing for collision resolution. It calculates the index using a hash function and probes the next available slot linearly until an empty slot is found.

| Method              | Description                                                          | Time Complexity | Space Complexity |
|---------------------|----------------------------------------------------------------------|-----------------|------------------|
| `insert(key, value)` | Inserts a key-value pair into the hash table using linear probing.  | O(1)            | O(1)             |
| `find(key)`         | Retrieves the value associated with the given key.                   | O(1)            | O(1)             |
| `update(key, value)`| Updates the value associated with the given key.                     | O(1)            | O(1)             |
| `delete(key)`       | Removes the key-value pair with the given key.                       | O(1)            | O(1)             |
| `list_all()`        | Returns a list of all values in the hash table.                      | O(n)            | O(n)             |


Note: n is the number of elements in the hash table.
