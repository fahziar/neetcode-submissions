class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, firstNumber in enumerate(numbers) :            
            for j in range(i+1, len(numbers)) :
                if firstNumber + numbers[j] == target :
                    return [i+1, j+1]
        
        return []
        