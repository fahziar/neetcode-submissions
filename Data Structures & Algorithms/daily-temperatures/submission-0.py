class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []

        for i in range(len(temperatures)):
            currentTemperature = temperatures[i]
            j = 1
            found = False

            while (not found) and (i + j < len(temperatures)) :
                if temperatures[i + j] > temperatures[i] :
                    found = True
                else : 
                    j += 1
            
            if found :
                result.append(j)
            else :
                result.append(0)
        
        return result

            
        