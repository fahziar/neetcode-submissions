class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def recursion(i, currNums, currSum) :
            # 0, [], 0
            if i == len(nums) :
                return
            
            currSum = currSum + nums[i] # 2

            if currSum > target :
                # backtrack
                return
            elif currSum == target :
                result.append(currNums + [nums[i]])
                return
            else :
                currNums.append(nums[i])
                for j in range(i, len(nums)) :
                    recursion(j, currNums, currSum)
                currNums.pop()
        
        for i in range(0, len(nums)) :
            recursion(i, [], 0)
        return result
        