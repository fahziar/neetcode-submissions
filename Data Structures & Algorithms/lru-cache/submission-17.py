class LRUCache:    

    def __init__(self, capacity: int):
        self.capacity = capacity # 2
        self.data = OrderedDict()
        

    def get(self, key: int) -> int:
        if key not in self.data :
            return -1
        
        self.data.move_to_end(key)
        return self.data[key]

    def put(self, key: int, value: int) -> None:
        if key in self.data :
            self.data[key] = value
            self.data.move_to_end(key)
        else :
            if self.capacity == len(self.data):
                self.data.popitem(last=False)
            self.data[key] = value


        
