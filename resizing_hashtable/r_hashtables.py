# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.count = 0

# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for char in string:
        hash = ((hash << 5) + hash) + ord(char)
    return hash % max

# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    hash_table_resize(hash_table)
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]

    while pair is not None and pair.key != key: 
        pair = pair.next

    if pair is None:
        new_pair = LinkedPair(key, value)
        head = hash_table.storage[index]
        hash_table.storage[index] = new_pair
        new_pair.next = head
    
        if new_pair is None:
            hash_table.count += 1

    else:
        pair = value
# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key, hash_table.capacity)
    pair = hash_table.storage[index]
    pre_pair = None

    if pair is not None:
        while pair is not None and pair.key != key:
            pre_pair = pair
            pair = pair.next

        if pre_pair is None and pair == key:
            hash_table.storage[index] = None
            hash_table.count -= 1
        elif pair is None:
            #warning if not found
            print(f"index {index} not found")

# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key, hash_table.capacity)

    pair = hash_table.storage[index]

    if pair is not None:
        while pair is not None and pair.key != key:
            pair = pair.next
        if pair is None:
            return None
        else:
            return pair.value
    else:
        print(f"key {key} not found")


# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    new_table = HashTable(hash_table.capacity * 2)

    for hash in range(hash_table.count):
        pair = hash_table.storage[hash]

        while pair is not None:
            hash_table_insert(new_table, pair.key, pair.value)
            pair = pair.next
            
    return new_table


def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()
