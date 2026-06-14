from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.keys = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keys[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keys[key] # [(10, 'value1')]

        if len(values) == 0 :
            return ""

        left = 0
        right = len(values) - 1
        candidate_idx = -1

        while left <= right :
            mid = (left + right) // 2 # 0

            if values[mid][0] == timestamp :
                return values[mid][1]
            elif values[mid][0] < timestamp :
                candidate_idx = mid
                left = mid + 1
            else :
                right = mid - 1
        
        print(candidate_idx)
        if candidate_idx != -1 :
            return values[candidate_idx][1]
        else:
            return ""
        
