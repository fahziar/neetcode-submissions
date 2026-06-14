class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.data = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.data :
            return -1
        
        self.data.move_to_end(key)
        return self.data[key]
        

    def put(self, key: int, value: int) -> None:
        if key not in self.data :
            if len(self.data) == self.capacity :
                self.data.popitem(last=False)
        else :
            self.data.move_to_end(key)
        self.data[key] = value
        


        
