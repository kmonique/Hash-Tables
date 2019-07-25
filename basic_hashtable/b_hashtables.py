

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
    for x in string:
        hash = ((hash << 5) + hash) + ord(x)
    print(hash % max)
    return hash % max

# '''
# Fill this in.

# If you are overwriting a value with a different key, print a warning.
# '''
def hash_table_insert(hash_table, key, value):
    #warning if already exists
    if value in hash_table.storage:
        print(f"Warning overwriting existing key for value: {value}")
        hash_table.length -= 1
    #add to hash_table
    index = hash(key, hash_table.capacity)
    pair = Pair(key, value)
    hash_table.storage[index] = pair
    print(f"insert hash key{hash_table.storage[index].key}")
    print(f"insert hash value{hash_table.storage[index].key}")
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
    print(f"retrieve hash key: {hash_table.storage[index]}")
    if hash_table.storage[index - 1] == None:
        print(f"failed")
        return None
    else:
        print(f"retrieve hash key: {hash_table.storage[index].key}")
        print(f"retrieve hash val: {hash_table.storage[index].value}")
    return hash_table.storage[index - 1]


def Testing():
    # ht = BasicHashTable(16)

    # hash_table_insert(ht, "line", "Here today...\n")

    # hash_table_remove(ht, "line")

    # if hash_table_retrieve(ht, "line") is None:
    #     print("...gone tomorrow (success!)")
    # else:
    #     print("ERROR:  STILL HERE")
    ht = BasicHashTable(8)
    hash_table_insert(ht, "key-0", "new-val-0")
    return_value = hash_table_retrieve(ht, "key-0")
    print(f"return val: {return_value}")
    # if hash_table_retrieve(ht, "new-val-0") is None:
    #     print("none")
    # else:
    #     print("True, value found")


Testing()