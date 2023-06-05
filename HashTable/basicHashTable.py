MAX_HASH_TABLE_SIZE = 4096
def get_index(data_list,a_string):
    
    result = 0

    for char in a_string:
        char_number = ord(char)
        result += char_number
    list_index = result%MAX_HASH_TABLE_SIZE
    return list_index

class BasicHashTable:
    
    def __init__(self,max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = [None] * max_size
    
    def insert(self,key,value):

        index = get_index(self.data_list, key)

        self.data_list[index] = (key,value)

    def find(self,key,value):
        index = get_index(self.data_list, key)

        kv = self.data_list[index]

        if not kv:
            return
        else:
            _,value = kv 
            return value
    def update(self,key,value):

        index = get_index(self.data_list, key)

        self.data_list[index] = (key,value)
    
    def delete(self,key):
        index = get_index(self.data_list, key)
        kv = self.data_list[index]

        if kv and kv[0] == key:
            self.data_list[index] = None
    
    def list_all(self):
        return [kv[0] for kv in self.data_list if not kv ]




basic_table = BasicHashTable(max_size=MAX_HASH_TABLE_SIZE)
# print(len(basic_table.data_list) == 1024)
basic_table.insert('Aakash', '9999999999')
basic_table.insert('Hemanth', '8888888888')
print(bool((basic_table.find("Aakash", '9999999999'))))
basic_table.delete('Aakash')
print(bool((basic_table.find("Aakash", '9999999999'))))
