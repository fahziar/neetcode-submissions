class Solution:
    def trap(self, height: List[int]) -> int:
        # (3,2,1,3)
        geLeft = [0] * len(height) # (0. )
        geRight = [0] * len(height)

        for i in range(1, len(height)) :
            geLeft[i] = max(height[i - 1], geLeft[i - 1])
        
        for i in range(len(height) - 2, -1, -1) :
            geRight[i] = max(height[i + 1], geRight[i + 1])
        
        totalWater = 0

        for i in range(len(height)) :
            lowestBorder = min(geRight[i], geLeft[i])

            trappedWater = lowestBorder - height[i]

            if trappedWater > 0 :
                totalWater += trappedWater
        
        return totalWater

            
        