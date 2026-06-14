class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        heapq.heapify(nums)
        self.data = nums
        self.k = k

        while len(self.data) > k :
            heapq.heappop(self.data)
        
        print(self.data)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.data, val)
        if len(self.data) > self.k :
            heapq.heappop(self.data)
        return self.data[0]
        
