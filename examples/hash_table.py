class HashTable:
    def __init__(self):
        self.size = 10  # Fixed size for the internal array (hash table)
        self.table = [[] for _ in range(self.size)]  # Each slot starts as an empty list

    # Simple hash function to map a key to an index
    def _hash(self, key):
        return hash(key) % self.size

    # Insert method for the hash table
    def insert(self, key, value):
        index = self._hash(key)  # Get the index using the hash function
        bucket = self.table[index]

        # Check if the key already exists in the bucket and update the value if it does
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                bucket[i] = (key, value)  # Update the value for the existing key
                return

        # If the key doesn't exist, append the new key-value pair to the bucket
        bucket.append((key, value))

    # Lookup method to find a value by key
    def lookup(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for k, v in bucket:
            if k == key:
                return v  # Return the value if the key is found

        return None  # Return None if the key is not found

    # Delete method to remove a key-value pair by key
    def delete(self, key):
        index = self._hash(key)
        bucket = self.table[index]

        for i, kv in enumerate(bucket):
            k, v = kv
            if k == key:
                del bucket[i]  # Remove the key-value pair from the bucket
                return True

        return False  # Return False if the key was not found

# Example usage:
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
hash_table.insert("city", "New York")

print("Name:", hash_table.lookup("name"))  # Output: Alice
print("Age:", hash_table.lookup("age"))    # Output: 30

hash_table.delete("city")
print("City:", hash_table.lookup("city"))  # Output: None