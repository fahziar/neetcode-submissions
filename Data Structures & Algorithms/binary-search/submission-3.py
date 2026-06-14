class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [-1,0,2,4,6,8], 1
        left = 0 # 0
        right = len(nums) - 1 # 5
        currIdx = right // 2 # 2

        while left <= right :
            if nums[currIdx] == target :
                return currIdx
            elif nums[currIdx] > target :
                right = currIdx - 1
                currIdx = (left + right) // 2
            else :
                left = currIdx + 1
                currIdx = (left + right) // 2
            
        
        return -1
        