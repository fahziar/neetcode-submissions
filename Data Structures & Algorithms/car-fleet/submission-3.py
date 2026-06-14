class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        carAndPosition = [(position[i], speed[i], (target - position[i]) / speed[i]) for i in range(len(position))]
        carAndPosition = sorted(carAndPosition, key=lambda pos: pos[0], reverse=True)

        fleetCount = 0
        prevArrivalTime = 0
        for pos in carAndPosition :
            if pos[2] > prevArrivalTime :
                fleetCount += 1
                prevArrivalTime = pos[2]
        
        return fleetCount