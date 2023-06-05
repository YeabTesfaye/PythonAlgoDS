MAX_HASH_TABLE_SIZE = 4096
def get_index(data_list, a_string):
    # Variable to store the result (updated after each iteration)
    result = 0
    
    for a_character in a_string:
        # Convert the character to a number (using ord)
        a_number = ord(a_character)
        # Update result by adding the number
        result += a_number
    
    # Take the remainder of the result with the size of the data list
    list_index = result % len(data_list)
    return list_index
def get_valid_index(data_list, key):
    # Start with the index returned by get_index
    index = get_index(data_list,key)
    
    while True:
        # Get the key-value pair stored at index
        kv = data_list[index]
        
        # If it is None, return the index
        if kv is None:
            return index
        
        # If the stored key matches the given key, return the index
        k, v = kv
        if k==key:
            return index
        
        # Move to the next index
        index += 1
        
        # Go back to the start if you have reached the end of the array
        if index == len(data_list):
            index = 0


class ProbingHashTable:
    
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    
    def insert(self,key,value):
        index = get_valid_index(self.data_list, key)

        self.data_list[index] = (key,value)
    
    def update(self,key,value):
        index = get_valid_index(self.data_list, key)

        self.data_list[index] = (key,value)

    def find(self,key):
        index = get_valid_index(self.data_list, key)

        kv = self.data_list[index]

        return None if not kv else kv[1]
    def delete(self,key):
        index = get_valid_index(self.data_list, key)

        kv = self.data_list[index]
        if kv and kv[0] == key:
            self.data_list[index] = None
    def list_all(self):
        return [kv[1] for kv in self.data_list if kv]

probing_table = ProbingHashTable()

# Insert a value
probing_table.insert('listen', 99)
probing_table.insert('silent', 990)
# Check the value
print(probing_table.find('listen') == 99 )
print(probing_table.find('silent'))

#delete the value
probing_table.delete('listen')
#check the value
print(probing_table.find('listen') == 99 )











