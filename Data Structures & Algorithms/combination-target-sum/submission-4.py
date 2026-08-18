class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        
        def recursive(i, currNums, currSum) :
            if i == len(nums) :
                return
    
            if currSum + nums[i] == target :
                currResult = currNums[:]
                currResult.append(nums[i])
                result.append(currResult)
            elif currSum + nums[i] < target :
                currNums.append(nums[i])
                currSum = currSum + nums[i]
                for i in range(i, len(nums)) :
                    recursive(i, currNums, currSum)
                currNums.pop()
        
        for i in range(0, len(nums)) :
            recursive(i, [], 0)
    
        return result
        