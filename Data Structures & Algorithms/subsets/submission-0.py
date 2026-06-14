class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        def subsetRecursive(i, prevSubset) :
            if i == len(nums) :
                return
            currSubset = list(prevSubset)

            # include current element
            currSubset.append(nums[i])
            result.append(currSubset)
            subsetRecursive(i+1, currSubset)

            # do not include current element
            subsetRecursive(i+1, prevSubset)
        
        subsetRecursive(0, [])

        return result

        