import json

class Node :
    def __init__(self, key, val, next=None, prev=None) :
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = {}
        self.head = None
        self.tail = None
    
    def _addToTail(self, node):
        if self.head == None :
            self.head = node
            self.tail = node
        else :
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    
    def _remove(self, node): 
        # disconnect from prev element
        if node.prev == None :
            self.head = node.next
        else :
            node.prev.next = node.next
        
        #disconnect from next element
        if node.next == None :
            self.tail = node.prev
        else :
            node.next.prev = node.prev
        
        node.next = None
        node.prev = None


    def get(self, key: int) -> int:
        if key not in self.data :
            return -1
        
        node = self.data[key]
        self._remove(node)
        self._addToTail(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.data :
            node = self.data[key]
            node.val = value
            self._remove(node)
        else :
            if len(self.data) == self.capacity :
                lruNode = self.head
                self._remove(lruNode)
                del self.data[lruNode.key]
            node = Node(key, value)
            self.data[key] = node
        self._addToTail(node)
