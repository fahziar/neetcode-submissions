class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temperature in enumerate(temperatures) :
            while stack and temperature > stack[-1][1] :
                stackIdx, stackT = stack.pop()
                result[stackIdx] = i - stackIdx
            stack.append((i, temperature))
        
        return result

            
        