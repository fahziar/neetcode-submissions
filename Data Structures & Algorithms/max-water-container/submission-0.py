class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        currentMax = 0
        i = 0
        j = len(heights) - 1

        while i < j:
            area = min(heights[j],heights[i]) * (j - i)
            currentMax = max(area, currentMax)

            if heights[i] > heights[j] :
                j -= 1
            else :
                i += 1
        
        return currentMax
        