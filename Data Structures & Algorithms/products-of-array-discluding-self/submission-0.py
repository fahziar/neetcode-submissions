class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums)) :
            accumulator = 1
            for j in range(0, len(nums)) :
                if j != i :
                    accumulator = accumulator * nums[j]
            
            result.append(accumulator)

        return result
        