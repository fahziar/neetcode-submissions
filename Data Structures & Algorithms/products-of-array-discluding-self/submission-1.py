class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)) :
            if i == 0 :
                result.append(1)
            else :
                result.append(result[i-1] * nums[i-1])

        accumulator = 1
        for i in range(len(nums) - 1, -1, -1) :
            if i != len(nums) - 1 :
                accumulator = accumulator * nums[i+1]
                result[i] = result[i] * accumulator

        return result
        