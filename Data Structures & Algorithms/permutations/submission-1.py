class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(currNums) :
            if len(currNums) == 0 :
                return [[]]
            
            currNum = currNums[0]
            currPermutation = recursive(currNums[1:])

            result = []
            for singlePermutation in currPermutation :
                for i in range(0, len(singlePermutation) + 1) :
                    curr = singlePermutation.copy()
                    curr.insert(i, currNum)
                    result.append(curr)
            
            return result
        
        return recursive(nums)
            
        