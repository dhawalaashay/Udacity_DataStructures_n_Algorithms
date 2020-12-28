class LRUCache:
    def __init__(self, maxSize):
        self.cache = dict()
        self.maxSize = maxSize
        #self.maxSize = maxSize or 1
        print(f"cache size set to - {maxSize}")
        if self.maxSize < 1:
            raise Exception("no data can be added to cache, as it's size is set to 0")
        self.currentSize = 0
        self.listOfMostRecent = DoublyLinkedList()

    def insertKeyValuePair(self, key, value):
        if key not in self.cache:
            if self.currentSize == self.maxSize:
                self.evictLeastRecent()
            else:
                self.currentSize += 1
            self.cache[key] = DoublyLinkedListNode(key, value)
        else:
            self.replaceKey(key, value)
        self.updateMostRecent(self.cache[key])

    def getValueFromKey(self, key):
        if key not in self.cache:
            return -1
        self.updateMostRecent(self.cache[key])
        return self.cache[key].value

    def getMostRecentKey(self):
        if self.listOfMostRecent.head is None:
            return -1
        return self.listOfMostRecent.head.key

    def evictLeastRecent(self):
        keyToRemove = self.listOfMostRecent.tail.key
        self.listOfMostRecent.removeTail()
        del self.cache[keyToRemove]

    def updateMostRecent(self, node):
        self.listOfMostRecent.setHeadTo(node)

    def replaceKey(self, key, value):
        if key not in self.cache:
            raise Exception("The provided key isn't in the cache !")
        self.cache[key].value = value


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHeadTo(self, node):
        if self.head == node:
            return
        elif self.head is None:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.prev = node
            self.head = node
            self.head.next = self.tail
        else:
            if self.tail == node:
                self.removeTail()
            node.removeBindings()
            self.head.prev = node
            node.next = self.head
            self.head = node

    def removeTail(self):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
            return
        self.tail = self.tail.prev
        self.tail.next = None


class DoublyLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

    def removeBindings(self):
        if self.prev is not None:
            self.prev.next = self.next
        if self.next is not None:
            self.next.prev = self.prev
        self.prev = None
        self.next = None


if __name__ == "__main__":
    maxsize = 5

    # testcase 1
    our_cache = LRUCache(maxsize)
    our_cache.insertKeyValuePair(1, 1)
    our_cache.insertKeyValuePair(2, 2)
    our_cache.insertKeyValuePair(3, 3)
    our_cache.insertKeyValuePair(4, 4)

    # returns 1
    print(our_cache.getValueFromKey(1))
    # returns 2
    print(our_cache.getValueFromKey(2))
    # returns -1 because 9 is not present in the cache
    print(our_cache.getValueFromKey(9))

    our_cache.insertKeyValuePair(5, 5)
    our_cache.insertKeyValuePair(6, 6)

    # returns -1 because 3 is not present in the cache, was removed which was the least recent key
    print(our_cache.getValueFromKey(3))
    print("\n***********************************************\n")

    # testcase 2, retrieving the same value again and again
    our_cache = LRUCache(maxsize)
    our_cache.insertKeyValuePair(1, 1)
    our_cache.insertKeyValuePair(2, 2)
    our_cache.insertKeyValuePair(3, 3)
    our_cache.insertKeyValuePair(4, 4)
    our_cache.insertKeyValuePair(5, 5)
    print(our_cache.getValueFromKey(3))
    print(our_cache.getValueFromKey(3))
    print(our_cache.getValueFromKey(3))
    print(our_cache.getValueFromKey(3))
    print(our_cache.getValueFromKey(3))
    print("\n***********************************************\n")

    # testcase 3, retrieving invalid values
    our_cache = LRUCache(maxsize)
    our_cache.insertKeyValuePair(1, 1)
    our_cache.insertKeyValuePair(2, 2)
    our_cache.insertKeyValuePair(3, 3)
    our_cache.insertKeyValuePair(4, 4)
    our_cache.insertKeyValuePair(5, 5)
    print(our_cache.getValueFromKey(55))
    print(our_cache.getValueFromKey(60))
    print(our_cache.getValueFromKey(30))
    print(our_cache.getValueFromKey(31))
    print(our_cache.getValueFromKey(35))
    print("\n***********************************************\n")

    # testcase 4 , size of the cache is set to 0
    minsize = 0
    new_cache = LRUCache(minsize)
    new_cache.insertKeyValuePair(1, 1)
    print(new_cache.getValueFromKey(1))
