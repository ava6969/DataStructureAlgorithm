import heapq


class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = {}
        self.storage_heap = []

    def set(self, key, value):
        if self.size == self.capacity:
            entry = heapq.nsmallest(1, self.storage.items(), lambda x: x[1][1])
            self.storage.pop(entry[0][0])
            self.storage[key] = (value, 0)
        else:
            self.storage[key] = (value, 0)
            self.size += 1

    def get(self, key):

        if key in self.storage:
            value, count = self.storage[key]
            self.storage[key] = (value, count + 1)
            return value
        else:
            return -1


def test():
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))  # returns 1
    print(our_cache.get(2))  # returns 2
    print(our_cache.get(9))  # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5)
    our_cache.set(6, 6)  # pop lowest frequency entry

    print(our_cache.get(3))  # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

test()