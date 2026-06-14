class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxSpeed = max(piles)
        minSpeed = 1 #1
        result = maxSpeed #25

        while minSpeed <= maxSpeed :
            currSpeed = (minSpeed + maxSpeed) // 2 # 13
            t = self.timeNeededToEat(piles, currSpeed)

            if t > h :
                minSpeed = currSpeed + 1
            elif t == h :
                result = currSpeed
                maxSpeed = currSpeed - 1
            else :
                result = currSpeed
                maxSpeed = currSpeed - 1
        
        return result
    
    def timeNeededToEat(self, piles, speed) :
        totalHour = 0 # 3
        for pile in piles :
            totalHour += -(pile // -speed)
        
        return totalHour
    
        