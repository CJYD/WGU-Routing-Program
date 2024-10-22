# Create Chaining Hash Map class
# Sourced from C950 - Webinar-1 Let's Go Hashing
# Hasp Map Chaining allows for multiple key value pairs to exist in the same "bucket"
class ChainingHashMap:
    # Constructor method to initialize the hash map
    # O(n) time complexity, where n is the initial capacity
    def __init__(self, init_cap=40):
        # Create an empty list to hold the buckets
        self.list = []
        for i in range(init_cap):
            self.list.append([])

    # Method to insert the key-value pair into the hash map
    # O(1) best case or O(n) worst case time complexity
    # Due to the possibilities of having the same bucket with many keys
    def insert(self, key, item):
        # Calculate the bucket index
        bucket = hash(key) % len(self.list)
        # Retrieve the bucket list at specified index
        bucket_list = self.list[bucket]

        # Iterate through the bucket list to check if key exists
        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = item  # Update existing key-value pair.
                return True

        # If key doesn't exist, create new key-value pair and append to the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Method to search for an item using its key in the hash map
    # O(1) best case or O(n) worst case time complexity
    # Due to the possibilities of having the same bucket with many keys
    def search(self, key):
        # Calculate the bucket index
        bucket = hash(key) % len(self.list)
        # Retrieve the bucket list at specified index
        bucket_list = self.list[bucket]

        # Iterate through the bucket list to find its value
        for pair in bucket_list:
            # If the key is found, return its value.
            if key == pair[0]:
                return pair[1]

        # If the key is not found, return None.
        return None

    # Method to remove a key-value pair from the hash map
    # O(1) best case or O(n) worst case time complexity
    # Due to the possibilities of having the same bucket with many keys
    def remove(self, key):
        # Calculate the bucket index
        bucket = hash(key) % len(self.list)
        # Retrieve the bucket list at specified index
        bucket_list = self.list[bucket]

        # Iterate through the bucket list to find the key
        if key in bucket_list:
            bucket_list.remove(key)