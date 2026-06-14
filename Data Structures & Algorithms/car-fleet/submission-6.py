class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        cars = sorted(zip(position, speed), reverse=True)

        for car in cars :
            arrivalTime = (target - car[0]) / car[1]
            if not fleets :
                fleets.append(arrivalTime)
            elif fleets[-1] < arrivalTime :
                fleets.append(arrivalTime)
        
        return len(fleets)
        