class Node :
    def __init__(self, key, val, next=None, prev=None) :
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.data = {}
    
    def remove(self, node) :
        if node.prev == None :
            self.head = node.next
        else :
            node.prev.next = node.next
        
        if node.next == None :
            self.tail = node.prev
        else :
            node.next.prev = node.prev
        
        node.prev = None
        node.next = None
    
    def appendToEnd(self, node) :
        if self.tail == None :
            self.head = node
            self.tail = node
        else :
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    

    def get(self, key: int) -> int:
        if key not in self.data :
            return -1
        
        node = self.data[key]
        self.remove(node)
        self.appendToEnd(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.data :
            node = self.data[key]
            node.val = value
            self.remove(node)
            self.appendToEnd(node)
        else :
            if self.capacity == len(self.data) :
                del self.data[self.head.key]
                self.remove(self.head)
            node = Node(key, value)
            self.appendToEnd(node)
            self.data[key] = node
        
