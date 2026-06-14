class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        stack = []

        for i, height in enumerate(heights) :
            if i == 0 :
                stack.append((i, height)) # [(0, 1), (2, 2), (4, 2), (4, 5)]
            else :
                startIdx = i # 5
                while stack and stack[-1][1] > height :
                    prevIdx, prevHeight = stack.pop() # 2, 7
                    prevArea = (i - prevIdx) * prevHeight # 7
                    maxArea = max(maxArea, prevArea) # 7
                    startIdx = prevIdx # 2
                
                stack.append((startIdx, height))
        
        # [(0, 1), (2, 2), (4, 2), (5, 4)]
        print(stack)
        for idx, height in stack :
            area = (len(heights) - idx) * height
            maxArea = max(area, maxArea)
        
        return maxArea