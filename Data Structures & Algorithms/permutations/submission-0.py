class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursive(currNums) :
            if len(currNums) == 0 :
                return [[]]
            
            currList = recursive(currNums[1:])
            firstNum = currNums[0]
            print(currNums[1:])

            result = []
            for permutation in currList :
                for i in range(len(permutation) + 1) :
                    copy = permutation.copy()
                    copy.insert(i, firstNum)
                    result.append(copy)
            
            return result

        return recursive(nums)


        