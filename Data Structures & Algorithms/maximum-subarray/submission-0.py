class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        currCount = nums[right]
        currMax = currCount

        right = right + 1
        while right < len(nums) :
            if currCount < 0 :
                left = right
                currCount = 0
            currCount = currCount + nums[right]
            right = right + 1
            currMax = max(currCount, currMax)
        
        return currMax