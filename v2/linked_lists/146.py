from LinkedList import ListNode, LinkedList

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = dict()

        # For the LRU Linked List
        self.head = None
        self.tail = None
        self.sz = 0

        self.capacity = capacity

        self.LL = LinkedList

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.update(key)

        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        self.update(key)

        # Puts the value in the cache
        self.cache[key] = value

        n = len(self.cache.keys())

        if n > self.capacity:
            self.cache.pop(self.head.val)

    def update(self, key: int) -> None:
        # Adding initial element
        if not self.tail:
            self.tail = self.head = ListNode(key)

        # Add key to the LL
        self.tail.next = ListNode(key)
        self.tail = self.tail.next
        self.sz += 1

        # Update head as necessary
        if self.sz == self.capacity:
            self.cnt[self.head.val] -= 1

            self.head = self.head.next
            self.sz -= 1


lRUCache = LRUCache(4)

lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.put(3, 3)

lRUCache.get(1)
lRUCache.get(2)
lRUCache.get(4)

lRUCache.put(4, 4)

lRUCache.get(1)
lRUCache.get(2)
lRUCache.get(3)
lRUCache.get(4)
lRUCache.get(2)

lRUCache.put(5, 5)

print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(5))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))

# print(lRUCache.put(6, 6))

# print(lRUCache.get(1))
# print(lRUCache.get(2))
# print(lRUCache.get(3))
# print(lRUCache.get(4))
# print(lRUCache.get(5))
# print(lRUCache.get(6))