# '''
# Basic hash table key/value pair
# '''
class Pair:
    def __init__(self, key, value):
        self.key = key
        self.value = value

# '''
# Basic hash table
# Fill this in.  All storage values should be initialized to None
# '''
class BasicHashTable:
    def __init__(self, capacity):
        #takes in the size of the array and creates a memeory slot equal to the size of the array
        self.capacity = capacity
        self.storage = [None] * capacity
        self.length = 0

# '''
# Fill this in.
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
    return hash % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    #create hash index and pair
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    #warning if already exists
    if hash_table.storage[index] != None:
        print(f"Warning overwriting existing key for value: {value}")
        hash_table.length -= 1
    #add to hash_table
    hash_table.storage[index] = pair
    #increase count
    hash_table.length += 1

# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    #if key/value is present set it to None
    if hash_table.storage[index] != None:
        hash_table.storage[index] = None
        hash_table.length -= 1
    else:
        #warning if not found
        print(f"index {index} not found")

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)
    if hash_table.storage[index] == None:
        return None
    return hash_table.storage[index].value


def Testing():
    ht = BasicHashTable(16)

    hash_table_insert(ht, "line", "Here today...\n")

    hash_table_remove(ht, "line")

    if hash_table_retrieve(ht, "line") is None:
        print("...gone tomorrow (success!)")
    else:
        print("ERROR:  STILL HERE")

Testing()