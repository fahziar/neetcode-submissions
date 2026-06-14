class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        prev = 0
        sum = digits[-1] + 1
        if sum >= 10 :
            sum = sum - 10
            prev = 1
        result.append(sum)
    
        for i in range(2, len(digits) + 1) : 
            sum = digits[-i] + prev
            if sum >= 10 :
                sum = sum - 10
                prev = 1
            else :
                prev = 0
            result.append(sum)
        
        if prev != 0 :
            result.append(prev)

        return result[::-1]
            
            
        