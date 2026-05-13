class MyHashSet:
    def __init__(self):
        self.buckets = [[] for _ in range(1000)]

    def add(self, key:int) -> None:
        bucket_index = key % 1000
        bucket = self.buckets[bucket_index]
        if key not in bucket:
            bucket.append(key)
       
    def remove(self, key:int) -> None:
        bucket_index = key % 1000
        bucket = self.buckets[bucket_index]
        if key in bucket:
            bucket.remove(key)
        
    def contains(self, key:int) -> bool:
        bucket_index = key % 1000
        bucket = self.buckets[bucket_index]
        return key in bucket
    

if __name__ == "__main__":
    myHashSet = MyHashSet()
    myHashSet.add(1)
    myHashSet.add(2)  
    print(myHashSet.contains(1))  # returns True
    print(myHashSet.contains(3))  # returns False (not found)
    myHashSet.add(2)
    print(myHashSet.contains(2))  # returns True
    myHashSet.remove(2)
    print(myHashSet.contains(2))  # returns False (already removed) 
