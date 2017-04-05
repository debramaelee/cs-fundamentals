class MyHashTable:
    def __init__(self):
        self.buckets = [None] * 26

    def my_hash(self, value):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        first_letter = value[0]
        return alphabet.index(first_letter.lower())

    def insert(self, value):
        # Inserts value into the correct bucket.
        
        # Get index of bucket
        idx = self.my_hash(value)

        # Initialize bucket as an array if bucket is None (first time inserts only)
        if self.buckets[idx] == None:
            self.buckets[idx] = []

        # append the value
        bucket = self.buckets[idx]
        bucket.append(value)


    def exists(self, value):
        # Returns true if the value exists in the bucket.
        idx = self.my_hash(value)
        bucket = self.buckets[idx]
        if bucket == None:
            return False
        for v in bucket:
            if v == value:
                return True
        return False
        # for i in range(len(self.buckets[idx])):
            
            # method 1
            # if i == value:
            #     True

            # method 2
            # if value == self.buckets[idx][i]:
            #     print True 
            # else:
            #     print False


hash_table = MyHashTable()
hash_table.insert('Hello World')
hash_table.insert('Bob')
hash_table.insert('Cathy')
hash_table.insert('Zebra')

print(hash_table.exists('Hello World'))

print(hash_table.buckets)